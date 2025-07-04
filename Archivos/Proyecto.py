import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar, END


def guardar_datos():
    nombre = entrada_nombre.get()
    apellido_paterno = entrada_apaterno.get()
    apellido_materno = entrada_amaterno.get()
    edad = entrada_edad.get()
    correo = entrada_correo.get()

    if not nombre or not apellidomaterno or not apellidopaterno or not edad or not correo:
        messagebox.showwarning("Campos vacíos", "Por favor ingresa tus datos.")
        return

    with open("datos.txt", "a") as archivo:
        archivo.write(f"{nombre:<20} {apellido_paterno:<20} {apellido_materno:<20}{edad:<2} {correo:<20}\n")

    entrada_nombre.delete(0, tk.END)
    entrada_apellidomaterno.delete(0, tk.END)
    entrada_apellidopaterno.delete(0, tk.END) # type: ignore
    entrada_edad.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    messagebox.showinfo("Guardado", "Datos guardados exitosamente.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Datos de usuario")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Apellido Paterno:").grid(row=1, column=0, padx=10, pady=5)
entrada_apellido = tk.Entry(ventana)
entrada_apellido.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Apellido Materno:").grid(row=2, column=0, padx=10, pady=5)
entrada_apellido = tk.Entry(ventana)
entrada_apellido.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Edad:").grid(row=3, column=0, padx=10, pady=5)
entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=3, column=1, padx=10, pady=5)

tk.Label(ventana, text="correo:").grid(row=4, column=0, padx=10, pady=5)
entrada_correo = tk.Entry(ventana)
entrada_correo.grid(row=4, column=1, padx=10, pady=5)

# Botón para guardar
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
btn_guardar.grid(row=4, column=0, columnspan=4, pady=10)

ventana.mainloop()
