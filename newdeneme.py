import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
from datetime import datetime

class PhotoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fotoğraf Denetleme Uygulaması")

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

        # Ana çerçeve
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")

        # Tarih ve saat etiketi
        self.date_label = ttk.Label(self.main_frame, font=('Helvetica', 10))
        self.date_label.pack(side="top", anchor="ne", padx=10, pady=5)

        # Sol alt köşedeki switcher butonu için çerçeve
        self.switcher_frame = ttk.Frame(self.main_frame)
        self.switcher_frame.pack(side="bottom", anchor="sw", padx=10, pady=10)

        # Arayüzü oluştur
        self.create_widgets()

        # Tarih ve saat güncellemesi
        self.update_datetime()

    def create_widgets(self):
        # Fotoğraf yükleme butonu
        load_button = ttk.Button(self.main_frame, text="Fotoğraf Yükle", command=self.load_image)
        load_button.pack(pady=10)

        # Fotoğrafı gösterme alanı
        self.image_label = ttk.Label(self.main_frame)
        self.image_label.pack(pady=10)

        # Fotoğrafı denetleme butonu
        process_button = ttk.Button(self.main_frame, text="Fotoğrafı Denetle", command=self.process_image)
        process_button.pack(pady=10)

        # Koyu ve açık modu ayarlayan buton
        mode_button = ttk.Button(self.switcher_frame, text="Koyu Mod" if not self.dark_mode.get() else "Açık Mod", command=self.toggle_mode)
        mode_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Fotoğraf Seç", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            self.image_path = file_path
            image = Image.open(file_path)
            image.thumbnail((300, 300))
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
        mode_button = self.switcher_frame.children['!button']
        mode_button.config(text="Koyu Mod" if not self.dark_mode.get() else "Açık Mod")

    def update_datetime(self):
        # Tarih ve saat etiketini güncelle
        now = datetime.now()
        formatted_datetime = now.strftime("%d-%m-%Y %H:%M:%S")
        self.date_label.config(text=formatted_datetime)
        # 1000 milisaniye (1 saniye) sonra güncelle
        self.root.after(1000, self.update_datetime)

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoApp(root)
    root.mainloop()
