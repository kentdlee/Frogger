from turtle import *

turtle = Turtle()
screen = turtle.getscreen()

turtle.color("green")
turtle.fillcolor("red")

turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-200,200)
turtle.pendown()

turtle.color("red")
turtle.fillcolor("blue")

turtle.begin_fill()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.end_fill()


screen.exitonclick()

