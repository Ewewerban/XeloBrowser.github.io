import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                             QHBoxLayout, QWidget, QLineEdit, 
                             QPushButton, QProgressBar)
from PyQt6.QtWebEngineWidgets import QWebEngineView

class VeloBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        # Tytuł okna i rozmiar startowy
        self.setWindowTitle("VeloBrowser – Fast & Minimal")
        self.setGeometry(100, 100, 1024, 768)

        # Główny widżet i układ (layout)
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Pasek nawigacji (przyciski i adres)
        self.nav_layout = QHBoxLayout()
        
        self.btn_back = QPushButton("←")
        self.btn_back.clicked.connect(self.back)
        self.nav_layout.addWidget(self.btn_back)

        self.btn_forward = QPushButton("→")
        self.btn_forward.clicked.connect(self.forward)
        self.nav_layout.addWidget(self.btn_forward)

        self.btn_reload = QPushButton("↻")
        self.btn_reload.clicked.connect(self.reload)
        self.nav_layout.addWidget(self.btn_reload)

        self.btn_home = QPushButton("⌂")
        self.btn_home.clicked.connect(self.navigate_home)
        self.nav_layout.addWidget(self.btn_home)

        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.navigate_to_url)
        self.nav_layout.addWidget(self.address_bar)

        self.layout.addLayout(self.nav_layout)

        # Pasek postępu ładowania strony (cienki niebieski pasek)
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumHeight(4)
        self.progress_bar.setTextVisible(False)
        self.layout.addWidget(self.progress_bar)

        # Okno przeglądarki (Silnik Chromium z Google)
        self.browser = QWebEngineView()
        self.browser.urlChanged.connect(self.update_address_bar)
        self.browser.loadProgress.connect(self.progress_bar.setValue)
        self.layout.addWidget(self.browser)

        # Strona startowa ustawiona na Google
        self.home_url = "https://www.google.com"
        self.browser.setUrl(QUrl(self.home_url))

    def navigate_home(self):
        self.browser.setUrl(QUrl(self.home_url))

    def navigate_to_url(self):
        url = self.address_bar.text()
        # Jeśli użytkownik nie wpisze http:// lub https://, dodajemy to automatycznie
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_address_bar(self, qurl):
        self.address_bar.setText(qurl.toString())

    def back(self):
        self.browser.back()

    def forward(self):
        self.browser.forward()

    def reload(self):
        self.browser.reload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VeloBrowser()
    window.show()
    sys.exit(app.exec())
