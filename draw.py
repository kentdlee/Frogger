from turtle import *

def drawSquare(t, sideLength):
    for i in range(4):
        t.forward(sideLength)
        t.right(90)    

def drawTriangle(t, sideLength):
    for i in range(3):
        t.forward(sideLength)
        t.left(120)    

def drawHexagon(t, sideLength):
    for i in range(6):
        t.forward(sideLength)
        t.left(60)    

def drawPolygon(t, sideLength, numberOfSides, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(numberOfSides):
        t.forward(sideLength)
        angle = 360 / numberOfSides
        t.left(angle)
    t.end_fill()
    
    
def main():
    t = Turtle()
    screen = t.getscreen()
    
    drawPolygon(t, 1, 200, "pink")
    
    drawSquare(t,100)   
    
    t.penup()
    t.goto(-200,200)
    t.pendown()
    
    t.color("red")
    t.fillcolor("blue")
    
    t.begin_fill()
    
    drawTriangle(t,100)
        
    t.end_fill()
    
    t.penup()
    t.goto(-200,-200)
    t.pendown()
    
    drawHexagon(t,60)   

    screen.exitonclick()
    
main()

