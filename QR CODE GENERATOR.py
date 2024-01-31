import tkinter as tk
import qrcode
from PIL import Image, ImageTk

class QRCodeGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR Code Generator")

        self.label = tk.Label(self, text="Enter text or link:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.generate_button = tk.Button(self, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()

        self.qr_label = tk.Label(self)
        self.qr_label.pack()

    def generate_qr_code(self):
        data = self.entry.get()
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((200, 200), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)

            self.qr_label.config(image=img)
            self.qr_label.image = img
        else:
            self.qr_label.config(text="Please enter some text or link")

if __name__ == "__main__":
    app = QRCodeGenerator()
    app.mainloop()