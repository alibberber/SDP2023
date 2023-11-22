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

        # Set the background color for the window
        self.window.configure(bg="black")

        # Create a frame with a black background
        self.frame = tk.Frame(window, bg="black")
        self.frame.pack(expand=True, fill="both")

        # Load an image to be displayed above "Select Photo" label
        image_path = "mef.jpeg"  # Replace with the actual path to your image
        self.logo_image = Image.open(image_path)
        self.logo_image = self.logo_image.resize((150, 150), Image.ANTIALIAS)
        self.tk_logo_image = ImageTk.PhotoImage(self.logo_image)

        # Create a label to display the image
        self.logo_label = tk.Label(self.frame, image=self.tk_logo_image, bg="black")
        self.logo_label.pack(pady=10)

        # Create GUI elements
        self.label = tk.Label(self.frame, text="Artificial Intelligence Supported Fire Control", bg="black", fg="white")
        self.label.pack(pady=10)

        self.photo_label = tk.Label(self.frame, text="Select a photo for Fire Control", bg="black", fg="white")
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
