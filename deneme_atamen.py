import tkinter as tk

# Tkinter penceresi oluşturuluyor
pencere = tk.Tk()

# Pencere boyutu ayarlanıyor
pencere.geometry("500x500")

# Etiket (Label) oluşturuluyor ve pencereye ekleniyor
etiket = tk.Label(pencere, text="Merhaba")
etiket.pack()

# Pencereyi görüntüle
pencere.mainloop()
