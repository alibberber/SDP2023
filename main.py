import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # Pillow kütüphanesi kullanılarak resim işleme

class YanginKontrolUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Yangın Kontrol Uygulaması")

        # Arayüz elemanlarını oluştur
        self.label = tk.Label(pencere, text="Yapay Zeka Destekli Yangın Kontrol")
        self.label.pack(pady=10)

        self.foto_label = tk.Label(pencere, text="Ateş Kontrolü için bir fotoğraf seçin.")
        self.foto_label.pack(pady=10)

        self.foto_button = tk.Button(pencere, text="Fotoğraf Seç", command=self.fotoSec)
        self.foto_button.pack(pady=10)

        self.baslat_button = tk.Button(pencere, text="Başlat", command=self.baslatFonksiyonu)
        self.baslat_button.pack(pady=10)

    def fotoSec(self):
        # Kullanıcıya dosya seçme penceresi göster
        dosya_yolu = filedialog.askopenfilename(filetypes=[("Resim Dosyaları", "*.png")])

        # Seçilen resmi ekranda göster
        if dosya_yolu:
            self.gosterResim(dosya_yolu)

    def gosterResim(self, dosya_yolu):
        resim = Image.open(dosya_yolu)
        resim = resim.resize((300, 300), Image.ANTIALIAS)
        tk_resim = ImageTk.PhotoImage(resim)

        # Eğer önceki bir resim varsa, güncelle
        if hasattr(self, 'resim_etiketi'):
            self.resim_etiketi.config(image=tk_resim)
            self.resim_etiketi.image = tk_resim
        else:
            self.resim_etiketi = tk.Label(self.pencere, image=tk_resim)
            self.resim_etiketi.pack(pady=10)

    def baslatFonksiyonu(self):
        # Burada fotoğraf üzerinde yangın kontrolü yapılacak işlemleri ekleyebilirsiniz.
        messagebox.showinfo("Başlatıldı", "Yangın kontrolü başlatıldı!")

if __name__ == "__main__":
    pencere = tk.Tk()
    uygulama = YanginKontrolUygulamasi(pencere)
    pencere.mainloop()
