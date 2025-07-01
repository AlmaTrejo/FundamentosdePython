import turtle as t

#Triangulo
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


mover(-50, 50)
t.color("blue")
for i in range(6):
    t.forward(100)
    t.left(60)
    t.hideturtle()
t.done()