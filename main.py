from book_recommender import BookRecommender

def main():
    recommender = BookRecommender()
    
    print("Kitap Öneri Sistemine Hoş Geldiniz!")
    print("Lütfen son okuduğunuz kitap hakkında düşüncelerinizi paylaşın:")
    
    while True:
        review = input("\nKitap yorumunuz (Çıkmak için 'q'): ")
        
        if review.lower() == 'q':
            break
            
        recommendation = recommender.analyze_review(review)
        print("\nSize özel kitap önerimiz:")
        print(f"Kitap: {recommendation['title']}")
        print(f"Yazar: {recommendation['author']}")
        print(f"Tür: {recommendation['genre']}")
        print(f"Açıklama: {recommendation['description']}")

if __name__ == "__main__":
    main() 