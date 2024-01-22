import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image , ImageTk


def generate_qr_code() :
    url = entry_url.get ( )

    qr = qrcode.QRCode (
        version=1 ,
        error_correction=qrcode.constants.ERROR_CORRECT_L ,
        box_size=10 ,
        border=4 ,
    )

    qr.add_data ( url )
    qr.make ( fit=True )

    img = qr.make_image ( fill_color="black" , back_color="white" )
    img_tk = ImageTk.PhotoImage ( img )
    qr_label.config ( image=img_tk )
    qr_label.image = img_tk

    messagebox.showinfo ( "QR Code Generated" , "QR Code has been generated successfully!" )


# Crear ventana
root = tk.Tk ( )
root.title ( "QR Code Generator" )

# Etiqueta y entrada para la dirección URL
url_label = tk.Label ( root , text="https://appestacionamientotest.firebaseapp.com/" )
url_label.pack ( )
entry_url = tk.Entry ( root )
entry_url.pack ( )

# Botón para generar el QR Code
generate_button = tk.Button ( root , text="Generate QR Code" , command=generate_qr_code )
generate_button.pack ( )

# Espacio para mostrar el QR Code
qr_label = tk.Label ( root )
qr_label.pack ( )

root.mainloop ( )
