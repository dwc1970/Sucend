import tkinter as tk
import sqlite3

# Función para enviar los datos a la base de datos SQLite
def enviar_datos():
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    primer_nombre = entrada_primer_nombre.get()
    saludo = entrada_saludo.get()
    whatsapp_url = entrada_enviar_whatsapp.get()

    # Conectar a la base de datos (o crearla si no existe)
    conexion = sqlite3.connect("datos_whatsapp.db")
    cursor = conexion.cursor()

    # Crear una tabla para almacenar los datos si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS contactos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_completo TEXT,
                        telefono TEXT,
                        primer_nombre TEXT,
                        saludo TEXT,
                        whatsapp_url TEXT
                    )''')

    # Insertar los datos en la base de datos
    cursor.execute("INSERT INTO contactos (nombre_completo, telefono, primer_nombre, saludo, whatsapp_url) VALUES (?, ?, ?, ?, ?)",
                   (nombre, telefono, primer_nombre, saludo, whatsapp_url))
    conexion.commit()
    conexion.close()

    # Limpiar los campos de entrada
    entrada_nombre.delete(0, tk.END)
    entrada_telefono.delete(0, tk.END)
    entrada_primer_nombre.delete(0, tk.END)
    entrada_saludo.delete(0, tk.END)
    entrada_enviar_whatsapp.delete(0, tk.END)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Envío de WhatsApp")
ventana.geometry("900x900")

# Crear etiquetas
etiqueta_nombre = tk.Label(ventana, text="Nombre completo:")
etiqueta_telefono = tk.Label(ventana, text="Teléfono:")
etiqueta_primer_nombre = tk.Label(ventana, text="Primer nombre:")
etiqueta_saludo = tk.Label(ventana, text="Saludo:")
etiqueta_enviar_whatsapp = tk.Label(ventana, text="Enviar vía WhatsApp Web:")

# Crear campos de entrada
entrada_nombre = tk.Entry(ventana)
entrada_telefono = tk.Entry(ventana)
entrada_primer_nombre = tk.Entry(ventana)
entrada_saludo = tk.Entry(ventana)
entrada_enviar_whatsapp = tk.Entry(ventana)

# Posicionar etiquetas y campos de entrada
etiqueta_nombre.pack()
entrada_nombre.pack()
etiqueta_telefono.pack()
entrada_telefono.pack()
etiqueta_primer_nombre.pack()
entrada_primer_nombre.pack()
etiqueta_saludo.pack()
entrada_saludo.pack()
etiqueta_enviar_whatsapp.pack()
entrada_enviar_whatsapp.pack()

# Botón para enviar los datos
boton_enviar = tk.Button(ventana, text="Enviar Datos", command=enviar_datos)
boton_enviar.pack()

# Ejecutar la ventana
ventana.mainloop()
