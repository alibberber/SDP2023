import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image

class YanginKontrolUygulamasi(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel('Yapay Zeka Destekli Yangın Kontrol')
        layout.addWidget(self.label)

        self.foto_label = QLabel('Ateş Kontrolü için bir fotoğraf seçin.')
        layout.addWidget(self.foto_label)

        self.foto_button = QPushButton('Fotoğraf Seç')
        self.foto_button.clicked.connect(self.fotoSec)
        layout.addWidget(self.foto_button)

        self.baslat_button = QPushButton('Başlat')
        self.baslat_button.clicked.connect(self.baslatFonksiyonu)
        layout.addWidget(self.baslat_button)

        self.setLayout(layout)

    def fotoSec(self):
        dosya_yolu, _ = QFileDialog.getOpenFileName(self, 'Fotoğraf Seç', '', 'Resim Dosyaları (*.png)')
        if dosya_yolu:
            self.gosterResim(dosya_yolu)

    def gosterResim(self, dosya_yolu):
        resim = Image.open(dosya_yolu)
        resim = resim.resize((300, 300), Image.ANTIALIAS)
        pixmap = QPixmap(resim)
        self.resim_label = QLabel(self)
        self.resim_label.setPixmap(pixmap)
        self.resim_label.show()

    def baslatFonksiyonu(self):
        # Burada fotoğraf üzerinde yangın kontrolü yapılacak işlemleri ekleyebilirsiniz.
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uygulama = YanginKontrolUygulamasi()
    uygulama.show()
    sys.exit(app.exec_())
