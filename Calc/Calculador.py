import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calcular():
    try:
        operacion = oper_var.get()
        numeros = [float(n) for n in entrada.get().split()]
        if not numeros:
            raise ValueError("Lista vacía")

        resultado = numeros[0]
        for num in numeros[1:]:
            if operacion == '+':
                resultado += num
            elif operacion == '-':
                resultado -= num
            elif operacion == '*':
                resultado *= num
            elif operacion == '/':
                if num == 0:
                    raise ZeroDivisionError
                resultado /= num
        
        resultado_var.set(f"Resultado: {resultado:.4f}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "División entre cero")
    except Exception as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

# Interfaz gráfica
ventana = Tk()
ventana.title("Calculadora ")

etq= tk.Label(ventana, text="Números separados por espacio:")
etq.grid()

tk.Label(ventana, text="Operación:")
oper_var = tk.StringVar(value="+")
tk.OptionMenu(ventana, oper_var, "+", "-", "*", "/").pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)
resultado_var = tk.StringVar()
tk.Label(ventana, textvariable=resultado_var, font=("Arial", 12)).pack()

ventana.mainloop()