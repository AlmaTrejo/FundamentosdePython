from tkinter import *
from tkinter import ttk
  
raiz = Tk()
raiz.title ("Inicio de Sesión")

marcoprincipal = ttk.Frame(raiz, padding= "3 3 12 12")
marcoprincipal.grid (column=0, row=0, sticky=(N, W, E, S))
marcoprincipal.columnconfigure (0, weight=1)
marcoprincipal.rowconfigure (0, weight=1)

nombre = StringVar()
contrasena = StringVar()

txtNombre = ttk.Entry(marcoprincipal, width=7, textvariable=nombre)
txtNombre.grid(column=2, row=1, sticky=(W, E))
txtContrasena = ttk.Entry(marcoprincipal, width=7, textvariable=contrasena)
txtContrasena.grid(column=2, row=2, sticky=(W, E))

ttk.Button(marcoprincipal, text= "Ingresar").grid(column=2, row=3, sticky=W)

ttk.Label(marcoprincipal, text="Usuario").grid(column=1, row=1, sticky=W)
ttk.Label(marcoprincipal, text="Contraseña").grid(column=1, row=2, sticky=E)

for child in marcoprincipal.winfo_children():
    child.grid_configure(padx=10, pady=10)

txtNombre.focus()
txtContrasena.focus()

raiz.mainloop()