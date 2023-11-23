import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
from datetime import datetime

class PhotoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fire Detection APP")

        # Değişkenler
        self.image_path = None
        self.dark_mode = tk.BooleanVar()
        self.dark_mode.set(False)

        # Ekran boyutları
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Pencere boyutları
        window_width = screen_width // 2
        window_height = screen_height // 2

        # Pencere konumu
        window_x = (screen_width - window_width) // 2
        window_y = (screen_height - window_height) // 2

        # Pencereyi ortala
        self.root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

        # Tema stilini uygula
        self.style = ThemedStyle(self.root)
        self.style.set_theme("plastik" if not self.dark_mode.get() else "equilux")

        # Tarih ve saat etiketi
        self.date_label = ttk.Label(self.root, text=self.get_current_datetime(), font=('Helvetica', 10))
        self.date_label.pack(side="top", anchor="ne", padx=10, pady=5)

        # Arayüzü oluştur
        self.create_widgets()

    def create_widgets(self):
        # Fotoğraf yükleme butonu
        load_button = ttk.Button(self.root, text="Fotoğraf Yükle", command=self.load_image)
        load_button.pack(pady=10)

        # Fotoğrafı gösterme alanı
        self.image_label = ttk.Label(self.root)
        self.image_label.pack(pady=10)

        # Fotoğrafı denetleme butonu
        process_button = ttk.Button(self.root, text="Fotoğrafı Denetle", command=self.process_image)
        process_button.pack(pady=10)

        # Koyu ve açık modu ayarlayan buton
        mode_button = ttk.Button(self.root, text="Koyu Mod" if not self.dark_mode.get() else "Açık Mod", command=self.toggle_mode)
        mode_button.pack(pady=10)

        # Tarih ve saat güncellemesi
        self.update_datetime()

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Fotoğraf Seç", filetypes=[("Image files", "*.png")])

        if file_path:
            self.image_path = file_path
            image = Image.open(file_path)
            image.thumbnail((300, 300))  # İstediğiniz boyutu ayarlayabilirsiniz
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def process_image(self):
        if self.image_path:
            # Fotoğraf işleme kodlarını buraya ekleyebilirsiniz
            # Örnek olarak, fotoğrafın adını ve boyutunu yazdıralım
            image = Image.open(self.image_path)
            print(f"Fotoğraf Adı: {image.filename}")
            print(f"Boyut: {image.size}")

    def toggle_mode(self):
        # Koyu ve açık modu değiştir
        self.dark_mode.set(not self.dark_mode.get())
        self.style.set_theme("plastik" if not self.dark_mode.get() else "equilux")
        mode_button = self.root.children['!button4']
        mode_button.config(text="Koyu Mod" if not self.dark_mode.get() else "Açık Mod")
        # Koyu ve açık mod için ilgili işlemleri ekleyebilirsiniz

    def update_datetime(self):
        # Tarih ve saat etiketini güncelle
        self.date_label.config(text=self.get_current_datetime())
        # 1000 milisaniye (1 saniye) sonra güncelle
        self.root.after(1000, self.update_datetime)

    def get_current_datetime(self):
        # Geçerli tarih ve saati al
        now = datetime.now()
        formatted_datetime = now.strftime("%d-%m-%Y %H:%M:%S")
        return formatted_datetime

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoApp(root)
    root.mainloop()
