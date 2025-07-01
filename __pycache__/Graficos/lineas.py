import turtle as t


t.pensize(2)
t.color("black")

def lineapunteada(longitud, punto=10, espacio=5):
    for _ in range(longitud // (punto + espacio)):
        t.pendown()
        t.forward(punto)
        t.penup()
        t.forward(espacio)
# Dibujar línea punteada horizontal
t.penup()
t.goto(-200, 0)  # Punto inicial
t.setheading(0)  # Apuntar hacia la derecha
lineapunteada(300)

# Dibujar flecha al final
t.pendown()
t.begin_fill()
t.forward(10)
t.left(135)
t.forward(15)
t.back(15)
t.right(270)
t.forward(15)
t.back(15)
t.left(135)
t.end_fill()

def lineapunteada(longitud, punto=10, espacio=5):
    for _ in range(longitud // (punto + espacio)):
        t.pendown()
        t.forward(punto)
        t.penup()
        t.forward(espacio)
# Dibujar línea punteada horizontal
t.penup()
t.goto(-150,100)  # Punto inicial
t.setheading(0)  # Apuntar hacia la derecha
lineapunteada(200)

# Dibujar flecha al final
t.pendown()
t.begin_fill()
t.forward(10)
t.left(135)
t.forward(15)
t.back(15)
t.right(270)
t.forward(15)
t.back(15)
t.left(135)
t.end_fill()



# Finalizar
t.hideturtle()
t.done()
