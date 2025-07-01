import turtle as t

#Triangulo
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

#triangulo
mover(-250, 50)
t.color("blue")
for i in range(3):
    t.forward(100)
    t.left(120)
#cuadrado
mover(-50, 50)
t.color("cyan")
for i in range(4):
    t.forward(100)
    t.left(90)

# Dibuja un pentágono
mover(150, 50)
t.color("pink")
for i in range(5):
    t.forward(100)
    t.left(72)

    t.hideturtle()
t.done()


