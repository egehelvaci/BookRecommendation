from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton,
                           QComboBox, QFrame, QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from book_recommender import BookRecommender
import sys

class BookRecommenderGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.recommender = BookRecommender()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Kitap Öneri Sistemi')
        self.setGeometry(100, 100, 1200, 800)
        
        # Ana widget ve layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Başlık
        title_label = QLabel('📚 Kitap Öneri Sistemi')
        title_label.setFont(QFont('Arial', 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Kitap arama bölümü
        search_layout = QHBoxLayout()
        search_label = QLabel('Kitap Adı:')
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Kitap adını girin...')
        self.search_button = QPushButton('Ara')
        self.search_button.clicked.connect(self.search_book)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)
        
        # Bulunan kitaplar için combobox
        self.books_combo = QComboBox()
        self.books_combo.setVisible(False)
        layout.addWidget(self.books_combo)
        
        # Seçilen kitap bilgileri
        self.book_info = QLabel()
        self.book_info.setWordWrap(True)
        self.book_info.setVisible(False)
        layout.addWidget(self.book_info)
        
        # Yorum bölümü
        review_label = QLabel('Kitap Hakkında Yorumunuz:')
        self.review_input = QTextEdit()
        self.review_input.setPlaceholderText('Düşüncelerinizi yazın...')
        layout.addWidget(review_label)
        layout.addWidget(self.review_input)
        
        # Öneri butonu
        self.recommend_button = QPushButton('Öneriler Al')
        self.recommend_button.clicked.connect(self.get_recommendations)
        layout.addWidget(self.recommend_button)
        
        # Öneriler için scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        self.recommendations_layout = QVBoxLayout(scroll_widget)
        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll)
        
        # Stil
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
                margin: 5px;
            }
            QLineEdit, QTextEdit {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 3px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QComboBox {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 3px;
                font-size: 14px;
            }
        """)
        
    def search_book(self):
        search_text = self.search_input.text()
        if search_text:
            matching_books = self.recommender.find_book_by_title(search_text)
            
            self.books_combo.clear()
            if matching_books:
                self.books_combo.setVisible(True)
                for book in matching_books:
                    self.books_combo.addItem(f"{book['title']} - {book['author']}", book)
                self.books_combo.currentIndexChanged.connect(self.show_book_info)
                self.show_book_info()
            else:
                self.book_info.setText("❌ Kitap bulunamadı!")
                self.book_info.setVisible(True)
                self.books_combo.setVisible(False)
    
    def show_book_info(self):
        if self.books_combo.currentData():
            book = self.books_combo.currentData()
            info = f"""
            📖 {book['title']}
            ✍️ Yazar: {book['author']}
            🏷️ Tür: {book['genre']}
            📝 Açıklama: {book['description']}
            """
            self.book_info.setText(info)
            self.book_info.setVisible(True)
    
    def get_recommendations(self):
        if not self.books_combo.currentData():
            return
            
        book = self.books_combo.currentData()
        review = self.review_input.toPlainText()
        
        if not review:
            return
            
        # Önceki önerileri temizle
        for i in reversed(range(self.recommendations_layout.count())): 
            self.recommendations_layout.itemAt(i).widget().setParent(None)
        
        # Yeni öneriler al
        recommendations, sentiment = self.recommender.analyze_review(book['title'], review)
        
        # Duygu analizi sonucunu göster
        sentiment_label = QLabel(f"📊 Yorum Analizi: {'Olumlu' if sentiment['label'] == 'POSITIVE' else 'Olumsuz'}")
        sentiment_label.setStyleSheet("font-weight: bold; color: #2196F3;")
        self.recommendations_layout.addWidget(sentiment_label)
        
        # Önerileri göster
        for i, rec in enumerate(recommendations, 1):
            frame = QFrame()
            frame.setFrameStyle(QFrame.Box | QFrame.Raised)
            frame.setStyleSheet("""
                QFrame {
                    background-color: white;
                    border-radius: 10px;
                    padding: 10px;
                    margin: 5px;
                }
            """)
            
            layout = QVBoxLayout(frame)
            
            title = QLabel(f"{i}. {rec['title']}")
            title.setFont(QFont('Arial', 12, QFont.Bold))
            layout.addWidget(title)
            
            author = QLabel(f"✍️ {rec['author']}")
            layout.addWidget(author)
            
            genre = QLabel(f"🏷️ {rec['genre']}")
            layout.addWidget(genre)
            
            desc = QLabel(rec['description'])
            desc.setWordWrap(True)
            layout.addWidget(desc)
            
            self.recommendations_layout.addWidget(frame)

def main():
    app = QApplication(sys.argv)
    gui = BookRecommenderGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 