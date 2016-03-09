from turtle import *

# f(x) = x * x

def drawSquare(turtle, x, y, sideLength, fillcolor):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(fillcolor) 
    turtle.begin_fill()    
    for i in range(4):
        turtle.forward(sideLength)
        turtle.right(90)  
    turtle.end_fill()
    
def drawTriangle(turtle, sideLength):
    for i in range(3):
        turtle.forward(sideLength)
        turtle.left(120)  
        
def drawHexagon(turtle, sideLength):
    for i in range(6):
        turtle.forward(sideLength)
        turtle.left(60)
        
def drawPolygon(turtle, x, y, sideLength, numberOfSides, fillcolor):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    angle = 360 / numberOfSides
    for i in range(numberOfSides):
        turtle.forward(sideLength)
    
        turtle.left(angle)
    turtle.end_fill()    
    
def main():
    turtle = Turtle()
    screen = turtle.getscreen()
    
    turtle.color("green")

    
    # y = f(2)
    drawSquare(turtle, 0,0, 100, "red")
    drawSquare(turtle, -300,-100, 50, "green")
    

    
    turtle.penup()
    turtle.goto(-200,200)
    turtle.pendown()
    
    turtle.color("red")
    turtle.fillcolor("blue")
    
    turtle.begin_fill()
    
    drawTriangle(turtle, 100)
    
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(200,200)
    turtle.pendown()
    turtle.fillcolor("purple")
    turtle.begin_fill()
    drawHexagon(turtle, 50)
    turtle.end_fill()
    
    
    
    drawPolygon(turtle, 200,-200,2,100,"grey")
    drawPolygon(turtle, 200,200,150,4,"dark blue")
    
    screen.exitonclick()
    
main()

