import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class FireControlApplication:
    def __init__(self, window):
        self.window = window
        self.window.title("Fire Control Application")

        # Set the window size to be half of the screen size
        window_width = self.window.winfo_screenwidth() // 2
        window_height = self.window.winfo_screenheight() // 2
        self.window.geometry(f"{window_width}x{window_height}")

        # Create a frame with a black background
        self.frame = tk.Frame(window)
        self.frame.pack(expand=True, fill="both")

        # Create GUI elements
        self.label = tk.Label(self.frame, text="Artificial Intelligence Supported Fire Control", fg="black")
        self.label.pack(pady=10)

        self.photo_label = tk.Label(self.frame, text="Select a photo for Fire Control", fg="black")
        self.photo_label.pack(pady=10)

        self.photo_button = tk.Button(self.frame, text="Select Photo", command=self.selectPhoto, bg="gray", fg="black")
        self.photo_button.pack(pady=10)

        self.start_button = tk.Button(self.frame, text="Start", command=self.startFunction, bg="gray", fg="black")
        self.start_button.pack(pady=10)

    def selectPhoto(self):
        # Show the file selection dialog to the user
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])

        # Display the selected image
        if file_path:
            self.showImage(file_path)

    def showImage(self, file_path):
        image = Image.open(file_path)
        image = image.resize((300, 300), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(image)

        # If there is a previous image, update it
        if hasattr(self, 'image_label'):
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image
        else:
            self.image_label = tk.Label(self.frame, image=tk_image, bg="black")
            self.image_label.pack(pady=10)

    def startFunction(self):
        # Add image processing for fire control here
        messagebox.showinfo("Started", "Fire control started!")

if __name__ == "__main__":
    window = tk.Tk()
    app = FireControlApplication(window)
    window.mainloop()
