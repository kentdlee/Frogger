from turtle import *

t = Turtle()
screen = t.getscreen()

for i in range(4):
    t.forward(100)
    t.right(90)
    

t.penup()
t.goto(-200,200)
t.pendown()

t.color("red")
t.fillcolor("blue")

t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)
    
t.end_fill()

t.penup()
t.goto(-200,-200)
t.pendown()

for i in range(6):
    t.forward(60)
    t.left(60)
    






screen.exitonclick()

