import sqlite3
import subprocess
import tkinter as tk

from PIL import Image , ImageTk
from tkcalendar import Calendar


def guardar_datos():
    nombre = entry_nombre.get()
    documento = entry_documento.get()
    direccion = entry_direccion.get()
    FechaCarga = cal_fecha_carga.get_date()
    FechaVence = cal_fecha_vence.get_date()
    usuario = "Usuario"
    observaciones = entry_observaciones.get()

    conn = sqlite3.connect('usuario.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE usuario
                      (ID INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR (20), documento VARCHAR(20), dirección VARCHAR(20),
                       FechaCarga VARCHAR(20), FechaVence VARCHAR(20), usuario VARCHAR(20), observaciones TEXT)''')
    cursor.execute('''INSERT INTO usuario VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (nombre, documento, direccion, FechaCarga, FechaVence, usuario, observaciones))
    conn.commit()
    conn.close()

    entry_nombre.delete(0, tk.END)
    entry_documento.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)
    entry_observaciones.delete(0, tk.END)

root = tk.Tk()
root.title("Venta y Mantenimiento de Matafuegos")
root.geometry("800x600")
root.configure(bg="beige")

imagen = Image.open("logo.jpg")
imagen = imagen.resize((20, 20), Image.LANCZOS)
icono = ImageTk.PhotoImage(imagen)
root.tk.call('wm', 'iconphoto', root._w, icono)

frame = tk.Frame(root, bg="sky blue")
frame.pack()

label_datos_personales = tk.Label(frame, text="Datos Personales", bg="sky blue", font=("Helvetica", 16, "bold"))
label_datos_personales.grid(row=0, columnspan=2, pady=10)

label_nombre = tk.Label(frame, text="Nombre y Apellidos:", bg="beige")
entry_nombre = tk.Entry(frame, width=30)
label_documento = tk.Label(frame, text="Documento:", bg="beige")
entry_documento = tk.Entry(frame, width=30)
label_direccion = tk.Label(frame, text="Dirección:", bg="beige")
entry_direccion = tk.Entry(frame, width=30)
label_observaciones = tk.Label(frame, text="Observaciones:", bg="beige")
entry_observaciones = tk.Entry(frame, width=30)

label_nombre.grid(row=1, column=0, pady=5, padx=20, sticky=tk.W)
entry_nombre.grid(row=1, column=1, pady=5)
label_documento.grid(row=2, column=0, pady=5, padx=20, sticky=tk.W)
entry_documento.grid(row=2, column=1, pady=5)
label_direccion.grid(row=3, column=0, pady=5, padx=20, sticky=tk.W)
entry_direccion.grid(row=3, column=1, pady=5)
label_observaciones.grid(row=4, column=0, pady=5, padx=20, sticky=tk.W)
entry_observaciones.grid(row=4, column=1, pady=5)

label_fechas = tk.Label(frame, text="Fechas", bg="beige", font=("Helvetica", 16, "bold"))
label_fechas.grid(row=5, columnspan=2, pady=10)

label_FechaCarga = tk.Label(frame, text="Fecha de Carga:", bg="beige")
cal_fecha_carga = Calendar(frame, date_pattern='yyyy-mm-dd')
label_FechaVence = tk.Label(frame, text="Fecha Vencimiento:", bg="beige")
cal_fecha_vence = Calendar(frame, date_pattern='yyyy-mm-dd')

label_FechaCarga.grid(row=6, column=0, pady=5, padx=20, sticky=tk.W)
cal_fecha_carga.grid(row=6, column=1, pady=5)
label_FechaVence.grid(row=7, column=0, pady=5, padx=20, sticky=tk.W)
cal_fecha_vence.grid(row=7, column=1, pady=5)

boton_guardar = tk.Button(frame, text="Guardar", command=lambda: abrir_archivo_y_cerrar_ventana())
boton_guardar.grid(row=30, pady=30, columnspan=2, padx=20)  # Centra el botón y lo extiende en dos columnas

def abrir_archivo_y_cerrar_ventana():
    subprocess.Popen(["python", "otros.py"])
    root.destroy()

root.mainloop()
