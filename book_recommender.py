from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import random
import time
from collections import defaultdict
from typing import List, Dict, Tuple, Any
import logging

# Logging ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BookRecommender:
    def __init__(self, cache_embeddings: bool = True):
        """
        Kitap öneri sistemi başlatıcı fonksiyonu.
        Args:
            cache_embeddings: Gömme vektörlerini önbellekte tutma seçeneği
        """
        logger.info("Kitap öneri sistemi başlatılıyor...")
        
        try:
            # Modelleri yükle
            self._load_models()
            
            # Veritabanını ve önbelleği yükle
            self._load_database()
            
            # Kitapları kategorize et
            self._categorize_books()
            
            # Gömme vektörlerini hesapla
            if cache_embeddings:
                self._cache_embeddings()
                
            logger.info("Sistem başarıyla başlatıldı!")
            
        except Exception as e:
            logger.error(f"Başlatma hatası: {e}")
            raise
    
    def _load_models(self):
        """AI modellerini yükle"""
        logger.info("Modeller yükleniyor...")
        
        self.sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="savasy/bert-base-turkish-sentiment-cased"
        )
        
        self.embedding_model = pipeline(
            "feature-extraction",
            model="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
        )
    
    def _load_database(self):
        """Kitap veritabanını yükle"""
        logger.info("Veritabanı yükleniyor...")
        
        try:
            with open('books_database.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.books_db = data['books']
        except FileNotFoundError:
            logger.error("books_database.json bulunamadı!")
            raise
    
    def _categorize_books(self):
        """Kitapları türlere ve yazarlara göre kategorize et"""
        self.books_by_genre = defaultdict(list)
        self.books_by_author = defaultdict(list)
        self.genre_keywords = defaultdict(set)
        
        for book in self.books_db:
            genre = book['genre']
            author = book['author']
            
            self.books_by_genre[genre].append(book)
            self.books_by_author[author].append(book)
            
            # Her tür için anahtar kelimeleri topla
            self.genre_keywords[genre].update(book['keywords'])
    
    def _cache_embeddings(self):
        """Kitap açıklamalarının gömme vektörlerini hesapla ve önbellekte tut"""
        logger.info("Gömme vektörleri hesaplanıyor...")
        
        self.embeddings_cache = {}
        total = len(self.books_db)
        
        for i, book in enumerate(self.books_db, 1):
            description = book['description']
            self.embeddings_cache[book['title']] = self.embedding_model(description)[0][0]
            
            if i % 10 == 0:
                logger.info(f"İşlenen: {i}/{total}")
    
    def get_recommendations(self, book_title: str, review: str) -> Tuple[List[Dict], Dict]:
        """
        Kitap önerileri ve duygu analizi sonuçlarını döndür
        Args:
            book_title: Okunan kitabın adı
            review: Kullanıcının yorumu
        Returns:
            Tuple[List[Dict], Dict]: Önerilen kitaplar ve duygu analizi sonucu
        """
        try:
            # Duygu analizi
            sentiment = self.sentiment_analyzer(review)[0]
            is_negative = sentiment['label'] == 'NEGATIVE'
            
            # Yorum vektörü
            review_embedding = self.embedding_model(review)[0][0]
            
            # Önerileri hesapla
            recommendations = self._get_smart_recommendations(
                book_title,
                review_embedding,
                is_negative,
                self._extract_keywords(review)
            )
            
            return recommendations, sentiment
            
        except Exception as e:
            logger.error(f"Öneri hatası: {e}")
            return self._get_fallback_recommendations(book_title), {'label': 'POSITIVE'}
    
    def _extract_keywords(self, text: str) -> Dict[str, set]:
        """Metinden anahtar kelimeleri çıkar"""
        words = set(text.lower().split())
        
        return {
            'positive': words & self.POSITIVE_WORDS,
            'negative': words & self.NEGATIVE_WORDS,
            'genre': words & self.GENRE_WORDS
        }
    
    def _get_smart_recommendations(self, 
                                 current_book: str,
                                 review_embedding: np.ndarray,
                                 is_negative: bool,
                                 keywords: Dict[str, set]) -> List[Dict]:
        """Akıllı kitap önerileri üret"""
        scores = {}
        current_book_data = next((b for b in self.books_db if b['title'] == current_book), None)
        
        if not current_book_data:
            return self._get_fallback_recommendations(current_book)
        
        # Her kitap için skor hesapla
        for book in self.books_db:
            if book['title'] == current_book:
                continue
                
            score = self._calculate_book_score(
                book,
                current_book_data,
                review_embedding,
                is_negative,
                keywords
            )
            
            scores[book['title']] = score
        
        # En iyi eşleşmeleri seç
        best_matches = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:20]
        
        # Çeşitlilik için rastgele seç
        selected = self._diverse_selection(best_matches, current_book_data)
        
        return [next(b for b in self.books_db if b['title'] == title) for title in selected]
    
    def _calculate_book_score(self,
                            book: Dict,
                            current_book: Dict,
                            review_embedding: np.ndarray,
                            is_negative: bool,
                            keywords: Dict[str, set]) -> float:
        """Bir kitap için benzerlik skorunu hesapla"""
        score = 0.0
        
        # İçerik benzerliği (0.35)
        content_sim = cosine_similarity(
            [review_embedding],
            [self.embeddings_cache[book['title']]]
        )[0][0]
        score += 0.35 * content_sim
        
        # Tür uyumu (0.25)
        if not is_negative:
            # Ana tür uyumu
            if book['genre'] == current_book['genre']:
                score += 0.15
            
            # İlişkili türler için bonus
            related_genres = {
                'polisiye': {'gerilim', 'macera', 'gizem'},
                'gerilim': {'polisiye', 'gizem', 'psikolojik'},
                'fantastik': {'macera', 'bilimkurgu'},
                'bilimkurgu': {'fantastik', 'distopya'},
                'psikolojik': {'modern', 'dram', 'gerilim'},
                'dram': {'psikolojik', 'roman'},
                'klasik': {'roman', 'dram'},
                'roman': {'dram', 'klasik'}
            }
            
            if book['genre'] in related_genres.get(current_book['genre'], set()):
                score += 0.10
        else:
            # Olumsuz yorumda farklı türlere yönlendir
            if book['genre'] != current_book['genre']:
                score += 0.25
        
        # Anahtar kelime uyumu (0.25)
        common_keywords = set(book['keywords']) & set(current_book['keywords'])
        unique_keywords = set(book['keywords']) - set(current_book['keywords'])
        
        # Ortak anahtar kelimeler için puan
        keyword_score = len(common_keywords) / len(book['keywords'])
        score += 0.15 * keyword_score
        
        # Benzersiz anahtar kelimeler için bonus
        if len(unique_keywords) >= 2:  # En az 2 farklı tema
            score += 0.10
        
        # Yazar çeşitliliği (0.10)
        if book['author'] != current_book['author']:
            score += 0.10
            
            # Aynı dönem/ülke yazarlarına küçük bonus
            if any(kw in book['keywords'] for kw in current_book['keywords'] 
                   if kw in ['türk', 'rus', 'fransız', 'ingiliz', 'modern', 'klasik']):
                score += 0.05
        
        # Popülerlik ve kalite faktörü (0.05)
        popular_authors = {
            'Agatha Christie', 'Arthur Conan Doyle', 'Dostoyevski', 
            'Orhan Pamuk', 'Stephen King', 'Dan Brown'
        }
        if book['author'] in popular_authors:
            score += 0.05
        
        return score
    
    def _diverse_selection(self, matches: List[Tuple[str, float]], current_book: Dict) -> List[str]:
        """Çeşitli kitap seçimi yap"""
        # Zaman ve mikrosaniye bazlı seed kullan
        seed = int((time.time() % 1) * 1000000)  # Mikrosaniye hassasiyetinde
        random.seed(seed)
        
        # En iyi 15 kitabı al ve karıştır
        top_matches = matches[:15]
        random.shuffle(top_matches)
        
        # Kitapları türlere göre grupla
        books_by_genre = defaultdict(list)
        for title, score in top_matches:
            book = next(b for b in self.books_db if b['title'] == title)
            books_by_genre[book['genre']].append((title, score))
        
        selected = []
        current_genre = current_book['genre']
        
        # İlk öneri için strateji seç
        strategy = random.random()  # 0-1 arası rastgele sayı
        
        if strategy < 0.4:  # %40 ihtimalle farklı türden seç
            other_genres = [g for g in books_by_genre.keys() if g != current_genre]
            if other_genres:
                genre = random.choice(other_genres)
                genre_books = books_by_genre[genre]
                if genre_books:
                    title, _ = random.choice(genre_books)
                    selected.append(title)
                
        elif strategy < 0.7:  # %30 ihtimalle en yüksek skorlu 5 kitaptan seç
            top_5 = top_matches[:5]
            if top_5:
                title, _ = random.choice(top_5)
                selected.append(title)
                
        else:  # %30 ihtimalle tamamen rastgele seç
            if top_matches:
                title, _ = random.choice(top_matches)
                selected.append(title)
        
        # İlk öneri seçilemediyse, varsayılan strateji
        if not selected and top_matches:
            title, _ = random.choice(top_matches[:5])
            selected.append(title)
        
        # İkinci öneri için kalan kitaplardan seç
        remaining_books = [(t, s) for t, s in top_matches if t not in selected]
        
        if remaining_books:
            # Skorları normalize et ve karesel ağırlıklandır
            total_score = sum(score for _, score in remaining_books)
            if total_score > 0:
                weights = [(score/total_score)**2 for _, score in remaining_books]
                title, _ = random.choices(
                    remaining_books,
                    weights=weights,
                    k=1
                )[0]
                selected.append(title)
        
        # Yeterli öneri yoksa yedek öneriler
        while len(selected) < 2:
            fallback_books = [b['title'] for b in self.books_db 
                             if b['title'] not in selected 
                             and b['title'] != current_book['title']
                             and b['genre'] in self.related_genres.get(current_book['genre'], {current_book['genre']})]
            if fallback_books:
                selected.append(random.choice(fallback_books))
            else:
                # Son çare: herhangi bir kitap
                all_books = [b['title'] for b in self.books_db 
                            if b['title'] not in selected 
                            and b['title'] != current_book['title']]
                if all_books:
                    selected.append(random.choice(all_books))
                else:
                    break
        
        # Global seed'i sıfırla
        random.seed()
        
        return selected
    
    # Sabit kelime listeleri
    POSITIVE_WORDS = {
        'güzel', 'harika', 'muhteşem', 'etkileyici', 'süper', 'sevdim',
        'başarılı', 'mükemmel', 'iyi', 'hoş', 'keyifli', 'sürükleyici',
        'beğendim', 'ilginç', 'değerli', 'önemli', 'derin', 'akıcı',
        'zevkli', 'eğlenceli', 'düşündürücü', 'yaratıcı', 'özgün',
        'başyapıt', 'tavsiye', 'öneririm', 'okumalı', 'mutlaka'
    }
    
    NEGATIVE_WORDS = {
        'kötü', 'sıkıcı', 'berbat', 'sevmedim', 'karanlık', 'bunaltıcı',
        'zayıf', 'başarısız', 'yetersiz', 'sıradan', 'vasat', 'gereksiz',
        'beğenmedim', 'anlamsız', 'yüzeysel', 'tekdüze', 'durağan',
        'yorucu', 'karmaşık', 'anlaşılmaz', 'hayal kırıklığı', 'zaman kaybı'
    }
    
    GENRE_WORDS = {
        'macera', 'aşk', 'polisiye', 'bilim', 'fantastik', 'tarihi',
        'gizem', 'gerilim', 'dram', 'komedi', 'felsefe', 'psikolojik'
    }

    def find_book_by_title(self, title: str) -> List[Dict]:
        """
        Başlığa göre kitap ara
        Args:
            title: Aranacak kitap başlığı
        Returns:
            List[Dict]: Eşleşen kitapların listesi
        """
        # Büyük/küçük harf duyarlılığını kaldır
        search_title = title.lower().strip()
        
        # Başlıkta arama yap
        matching_books = [
            book for book in self.books_db 
            if search_title in book['title'].lower().strip()
        ]
        
        # Tam eşleşme varsa sadece onu döndür
        exact_matches = [
            book for book in matching_books
            if search_title == book['title'].lower().strip()
        ]
        
        if exact_matches:
            return exact_matches
        
        return matching_books

    def _get_fallback_recommendations(self, current_book: str) -> List[Dict]:
        """Yedek öneri sistemi"""
        try:
            current_genre = next((b['genre'] for b in self.books_db if b['title'] == current_book), None)
            similar_books = [b for b in self.books_db 
                           if b['genre'] == current_genre and b['title'] != current_book]
            return random.sample(similar_books, min(2, len(similar_books)))
        except Exception as e:
            logger.error(f"Yedek öneri hatası: {e}")
            return random.sample(self.books_db, 2)

    def analyze_review(self, book_title: str, review: str) -> Tuple[List[Dict], Dict]:
        """
        Kullanıcı yorumunu analiz edip kitap önerileri üret
        """
        logger.info(f"'{book_title}' için yorum analizi yapılıyor...")
        
        try:
            # Duygu analizi için metin ön işleme
            processed_review = self._preprocess_review(review)
            
            # Duygu analizi yap
            sentiment_scores = []
            
            # Cümlelere ayır ve her cümle için analiz yap
            sentences = [s.strip() for s in review.split('.') if s.strip()]
            for sentence in sentences:
                sentiment = self.sentiment_analyzer(sentence)[0]
                score = 1 if sentiment['label'] == 'POSITIVE' else -1
                confidence = sentiment['score']
                sentiment_scores.append(score * confidence)
            
            # Genel duygu skorunu hesapla
            if sentiment_scores:
                # Pozitif kelime sayısı ve ağırlıkları
                positive_words = []
                for word in review.lower().split():
                    if word in self.POSITIVE_WORDS:
                        weight = 2.0 if word in {'çok', 'süper', 'muhteşem', 'harika'} else 1.0
                        positive_words.append(weight)
                
                # Negatif kelime sayısı ve ağırlıkları
                negative_words = []
                for word in review.lower().split():
                    if word in self.NEGATIVE_WORDS:
                        weight = 2.0 if word in {'berbat', 'kötü', 'rezalet'} else 1.0
                        negative_words.append(weight)
                
                # "Beğendim" ve benzeri ifadeleri kontrol et
                positive_phrases = [
                    'beğendim', 'sevdim', 'güzeldi', 'hoşuma gitti', 
                    'sürükleyici', 'etkileyici', 'başarılı'
                ]
                
                for phrase in positive_phrases:
                    if phrase in review.lower():
                        positive_words.append(2.0)  # Güçlü pozitif ağırlık
                
                # Ağırlıklı skor hesapla
                pos_score = sum(positive_words)
                neg_score = sum(negative_words)
                
                # Model skoru ve kelime skoru birleştir
                avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
                word_sentiment = (pos_score - neg_score) / (pos_score + neg_score + 1)
                
                # Pozitif yanlılık ekle (threshold değerini düşür)
                final_score = (avg_sentiment * 0.6) + (word_sentiment * 0.4)
                
                sentiment_result = {
                    'label': 'POSITIVE' if final_score > -0.2 else 'NEGATIVE',
                    'score': abs(final_score)
                }
                
                # Eğer pozitif ifadeler varsa zorla pozitif yap
                if pos_score > 0 and neg_score == 0:
                    sentiment_result['label'] = 'POSITIVE'
            
            else:
                sentiment_result = {'label': 'POSITIVE', 'score': 0.5}
            
            # Yorum vektörünü hesapla
            review_embedding = self.embedding_model(processed_review)[0][0]
            
            # Anahtar kelimeleri çıkar
            keywords = self._extract_keywords(review)
            
            # Akıllı önerileri al
            recommendations = self._get_smart_recommendations(
                book_title,
                review_embedding,
                sentiment_result['label'] == 'NEGATIVE',
                keywords
            )
            
            return recommendations, sentiment_result
            
        except Exception as e:
            logger.error(f"Yorum analizi hatası: {e}")
            return self._get_fallback_recommendations(book_title), {'label': 'POSITIVE', 'score': 0.5}

    def _preprocess_review(self, review: str) -> str:
        """Yorumu duygu analizi için hazırla"""
        # Küçük harfe çevir
        text = review.lower()
        
        # Pozitif ifadeleri güçlendir
        for word in self.POSITIVE_WORDS:
            if word in text:
                text = text.replace(word, f"{word} {word}")
        
        # Emoji ve özel karakterleri yorumla
        emoji_map = {
            '👍': 'çok iyi',
            '❤️': 'harika',
            '😊': 'güzel',
            '👎': 'kötü',
            '😔': 'üzücü',
            '!': ' ünlem ',
            '?': ' soru '
        }
        
        for emoji, replacement in emoji_map.items():
            text = text.replace(emoji, f" {replacement} ")
        
        return text

def main():
    recommender = BookRecommender()
    
    print("\n📚 Kitap Öneri Sistemine Hoş Geldiniz! 📚")
    
    # Kitapları türlerine göre grupla
    genres = {}
    for book in recommender.books_db:
        genre = book['genre']
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(book)
    
    # Türlere göre kitapları listele
    print("\nMevcut Kitaplar (Türlere Göre):")
    for genre, books in genres.items():
        print(f"\n📑 {genre.upper()}:")
        for book in books:
            print(f"  • {book['title']} - {book['author']}")
    
    while True:
        print("\nLütfen okuduğunuz kitabın adını girin:")
        book_title = input("Kitap adı (Çıkmak için 'q'): ")
        
        if book_title.lower() == 'q':
            break
        
        # Kitabı bul
        matching_books = recommender.find_book_by_title(book_title)
        
        if not matching_books:
            print("\n❌ Bu kitabı veritabanımızda bulamadık.")
            print("İpucu: Kitap adının bir kısmını yazabilirsiniz.")
            continue
        
        # Birden fazla sonuç varsa kullanıcıya seçtir
        if len(matching_books) > 1:
            print("\nBirden fazla kitap bulundu:")
            for i, book in enumerate(matching_books, 1):
                print(f"{i}. {book['title']} - {book['author']}")
            
            choice = int(input("\nLütfen bir numara seçin: ")) - 1
            selected_book = matching_books[choice]
        else:
            selected_book = matching_books[0]
        
        print(f"\n📖 Seçilen Kitap: {selected_book['title']}")
        print(f"✍️ Yazar: {selected_book['author']}")
        
        print("\nBu kitap hakkındaki düşüncelerinizi paylaşın:")
        review = input("Yorumunuz: ")
        
        recommendation, sentiment = recommender.analyze_review(selected_book['title'], review)
        
        # Sonuçları göster
        print("\n📊 Yorum Analizi:")
        print(f"Duygu: {'Olumlu' if sentiment['label'] == 'POSITIVE' else 'Olumsuz'}")
        
        print("\n🎯 Size Özel Kitap Önerilerimiz:")
        print("\n1️⃣ İlk Önerimiz:")
        print(f"📚 {recommendation[0]['title']}")
        print(f"✍️ {recommendation[0]['author']}")
        print(f"📝 {recommendation[0]['description']}")
        print(f"🏷️ Tür: {recommendation[0]['genre']}")
        
        print("\n2️⃣ İkinci Önerimiz:")
        print(f"📚 {recommendation[1]['title']}")
        print(f"✍️ {recommendation[1]['author']}")
        print(f"📝 {recommendation[1]['description']}")
        print(f"🏷️ Tür: {recommendation[1]['genre']}")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    main() 