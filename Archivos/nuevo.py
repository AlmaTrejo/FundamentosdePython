import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar, END

def guardar_datos():
    nombre = entrada_nombre.get()
    apellido_paterno = entrada_apellido_paterno.get()
    apellido_materno = entrada_apellido_materno.get()
    edad = entrada_edad.get()
    ocupacion = ocupacion_var.get()
    correo = entrada_correo.get()
    telefono = entrada_telefono.get()

    if not all([nombre, apellido_paterno, apellido_materno, edad, ocupacion, correo, telefono]):
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return

    if not edad.isdigit():
        messagebox.showwarning("Edad no aceptable", "La edad debe ser un número.")
        return

    with open("datos.txt", "a") as archivo:
        archivo.write(f"{nombre:<15} {apellido_paterno:<15} {apellido_materno:<15} {edad:<5} {ocupacion:<15} {correo:<25} {telefono:<15}\n")

    for campo in [entrada_nombre, entrada_apellido_paterno, entrada_apellido_materno, entrada_edad, entrada_correo, entrada_telefono]:
        campo.delete(0, END)
    ocupacion_var.set(opciones_ocupacion[0])

    messagebox.showinfo("Guardado", "Datos guardados exitosamente.")

def mostrar_datos():
    try:
        with open("datos.txt", "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo de datos.")
        return

    ventana_datos = Toplevel(ventana)
    ventana_datos.title("Datos guardados")

    texto = Text(ventana_datos, wrap="none", width=130, height=20)
    texto.insert(END, "Nombre         Ap. Paterno     Ap. Materno     Edad  Ocupación       Correo                   Teléfono\n")
    texto.insert(END, "-"*120 + "\n")
    texto.insert(END, contenido)
    texto.config(state="disabled")
    texto.pack(side="left", fill="both", expand=True)

    scrollbar = Scrollbar(ventana_datos, command=texto.yview)
    texto.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

# Ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")

campos = [
    ("Nombre:", 0), ("Apellido Paterno:", 1),
    ("Apellido Materno:", 2), ("Edad:", 3),
    ("Correo:", 4), ("Teléfono:", 5)
]

entrada_nombre = tk.Entry(ventana)
entrada_apellido_paterno = tk.Entry(ventana)
entrada_apellido_materno = tk.Entry(ventana)
entrada_edad = tk.Entry(ventana)
entrada_correo = tk.Entry(ventana)
entrada_telefono = tk.Entry(ventana)

entradas = [entrada_nombre, entrada_apellido_paterno, entrada_apellido_materno, entrada_edad, entrada_correo, entrada_telefono]

for (texto, fila), entrada in zip(campos, entradas):
    tk.Label(ventana, text=texto).grid(row=fila, column=0, padx=10, pady=5)
    entrada.grid(row=fila, column=1, padx=10, pady=5)

tk.Label(ventana, text="Ocupación:").grid(row=0, column=2, padx=10, pady=5)
opciones_ocupacion = ["Elije opcion", "Estudiante", "Empleado", "Desempleado"]
ocupacion_var = tk.StringVar(value=opciones_ocupacion[0])
menu_ocupacion = tk.OptionMenu(ventana, ocupacion_var, *opciones_ocupacion)
menu_ocupacion.grid(row=1, column=2, padx=10, pady=5)

btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
btn_guardar.grid(row=7, column=2, pady=10)

btn_mostrar = tk.Button(ventana, text="Muestra datos", command=mostrar_datos)
btn_mostrar.grid(row=7, column=3, pady=10)

ventana.mainloop()

