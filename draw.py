from turtle import *

# f(x) = x * x
class Square:
    def __init__(self, x, y, sideLength, fillcolor):
        self.x = x
        self.y = y
        self.sideLength = sideLength
        self.fillcolor = fillcolor
        
    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.fillcolor(self.fillcolor) 
        turtle.begin_fill()    
        for i in range(4):
            turtle.forward(self.sideLength)
            turtle.right(90)  
        turtle.end_fill()        
        

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
    
class Triangle:
    def __init__(self,sideLength):
        self.sideLength = sideLength
        
    def draw(self, turtle):
        for i in range(3):
            turtle.forward(self.sideLength)
            turtle.left(120)         
        
    
def drawTriangle(turtle, sideLength):
    for i in range(3):
        turtle.forward(sideLength)
        turtle.left(120)  
        
def drawHexagon(turtle, sideLength):
    for i in range(6):
        turtle.forward(sideLength)
        turtle.left(60)
       

class Polygon:
    def __init__(self,x, y, sideLength, numberOfSides, fillcolor):
        self.x = x
        self.y = y
        self.sideLength = sideLength
        self.numberOfSides = numberOfSides
        self.fillcolor = fillcolor
        
    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        angle = 360 / self.numberOfSides
        for i in range(self.numberOfSides):
            turtle.forward(self.sideLength)
        
            turtle.left(angle)
        turtle.end_fill()         
        
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
    #drawSquare(turtle, 0,0, 100, "red")
    sq = Square(0,0,100,"red")
    sq.draw(turtle)
    #drawSquare(turtle, -300,-100, 50, "green")
    sq2 = Square(-300,-100,50,"green")
    sq2.draw(turtle)
    

    
    turtle.penup()
    turtle.goto(-200,200)
    turtle.pendown()
    
    turtle.color("red")
    turtle.fillcolor("blue")
    
    turtle.begin_fill()
    
    #drawTriangle(turtle, 100)
    tri = Triangle(100)
    tri.draw(turtle)
    
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(200,200)
    turtle.pendown()
    turtle.fillcolor("purple")
    turtle.begin_fill()
    drawHexagon(turtle, 50)
    turtle.end_fill()
    
    
    
    #drawPolygon(turtle, 200,-200,2,100,"grey")
    #drawPolygon(turtle, 200,200,150,4,"dark blue")
    
    p1 = Polygon(200,-200,2,100,"grey")
    p2 = Polygon(200,200,150,4,"dark blue")
    p1.draw(turtle)
    p2.draw(turtle)
    
    screen.exitonclick()
    
main()

