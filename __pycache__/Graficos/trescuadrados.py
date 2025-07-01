import turtle as t

def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

#cuadrado

for i in range(3):
    mover(-50, 50)
    t.left(20)
    t.color("black")
    for j in range(4):
        t.forward(100)
        t.left(90)

    t.hideturtle()
t.done()