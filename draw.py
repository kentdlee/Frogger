from turtle import *

t = Turtle()
screen = t.getscreen()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.penup()
t.goto(-200,200)
t.pendown()

t.color("red")
t.fillcolor("blue")

t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()




screen.exitonclick()

