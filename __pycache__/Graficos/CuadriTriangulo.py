import turtle as t

def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

#cuadrado
mover(0, 0)
for i in range(4):
    t.color("black")
    t.forward(100)
    t.left(90)
mover(100,100)
for i in range(2):
    t.color("black")
    t.left(120)
    t.forward(100)
    
mover(0, 0)
t.left(165)
t.forward(144)
mover(100,0)
t.left(90)
t.forward(144)

t.hideturtle()
t.done()