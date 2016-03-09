from turtle import *

turtle = Turtle()
screen = turtle.getscreen()

turtle.color("green")
turtle.fillcolor("red")

turtle.begin_fill()

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.end_fill()

turtle.penup()
turtle.goto(-200,200)
turtle.pendown()

turtle.color("red")
turtle.fillcolor("blue")

turtle.begin_fill()

for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.end_fill()

turtle.penup()
turtle.goto(200,200)
turtle.pendown()
turtle.fillcolor("purple")
turtle.begin_fill()
for i in range(6):
    turtle.forward(50)
    turtle.left(60)
turtle.end_fill()

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
turtle.fillcolor("grey")
turtle.begin_fill()
for i in range(100):
    turtle.forward(2)
    turtle.left(3.6)
turtle.end_fill()

screen.exitonclick()

