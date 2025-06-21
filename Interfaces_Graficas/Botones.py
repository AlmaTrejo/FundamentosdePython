from tkinter import *
from tkinter import ttk

raiz = Tk()
boton = ttk.Button(raiz, text ="Botón solo texto")
boton.grid()

imagen = PhotoImage(file="C:/Users/famar/Documents/IA Maestría/Ejercicios/FundamentosdePython/Interfaces_Graficas/kawaii-4.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image'] =imagen

btnCombinada = ttk.Button(raiz, text="Boton Combinado", compound="bottom")
btnCombinada.grid()
btnCombinada['image'] = imagen

chkBoton =ttk.Checkbutton(raiz, text="Opcion 1")
chkBoton.grid()

raiz.mainloop()