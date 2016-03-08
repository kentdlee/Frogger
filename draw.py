from turtle import *

def drawSquare(t, sideLength):
    for i in range(4):
        t.forward(sideLength)
        t.right(90)    
        
class Square:
    def __init__(self, sideLength):
        self.sideLength = sideLength
        
    def draw(self, t):
        for i in range(4):
            t.forward(self.sideLength)
            t.right(90)          
        

def drawTriangle(t, sideLength):
    for i in range(3):
        t.forward(sideLength)
        t.left(120)    
        
class Triangle:
    def __init__(self,sideLength):
        self.sideLength = sideLength
        
    def draw(self,t):
        for i in range(3):
            t.forward(self.sideLength)
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
    
class Polygon:
    def __init__(self, sideLength, numberOfSides, color):
        self.sideLength = sideLength
        self.numberOfSides = numberOfSides
        self. color = color
        
    def draw(self, t):
        t.fillcolor(self.color)
        t.begin_fill()
        for i in range(self.numberOfSides):
            t.forward(self.sideLength)
            angle = 360 / self.numberOfSides
            t.left(angle)
        t.end_fill()        
        
    
    
def main():
    t = Turtle()
    screen = t.getscreen()
    screen.tracer(0)
    
    #drawPolygon(t, 1, 200, "pink")
    poly = Polygon(1, 200, "pink")
    poly.draw(t)
    
    t.penup()
    t.goto(100,200)
    t.pendown()
    poly.draw(t)
    #drawSquare(t,100)   
    sq = Square(100)
    sq.draw(t)
    
    t.penup()
    t.goto(-200,200)
    t.pendown()
    
    t.color("red")
    t.fillcolor("blue")
    
    t.begin_fill()
    
    #drawTriangle(t,100)
    tri = Triangle(100)
    tri.draw(t)
        
    t.end_fill()
    
    t.penup()
    t.goto(-200,-200)
    t.pendown()
    
    drawHexagon(t,60)   

    screen.update()
    screen.exitonclick()
    
main()

