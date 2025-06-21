from tkinter import *
from tkinter import ttk

raiz =Tk()
etqTexto = ttk.Label(raiz, text="Etiqueta solo texto")
etqTexto.grid()

imagen = PhotoImage(file="C:/Users/famar/Documents/IA Maestría/Ejercicios/FundamentosdePython/Interfaces_Graficas/kawaii-4.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada =ttk.Label(raiz, text="Etq Combinada", compound= "center")
etqCombinada.grid()

etqCombinada['image']= imagen

raiz.mainloop()