from turtle import *
import tkinter
import math

class Frog(RawTurtle):
    def __init__(self,canvas):
        super().__init__(canvas)
        self.shape("images/frogger.gif")
        self.left(90)
        self.penup()
        self.goto(0,-250)
        
class RaceCar(RawTurtle):
    def __init__(self,canvas,x,y):
        super().__init__(canvas)
        self.shape("images/racecar.gif")
        self.left(180)
        self.penup()
        self.goto(x,y)
        
    def forward(self, distance):
        if self.xcor() < -400:
            self.goto(400,self.ycor())
            
        super().forward(distance)
      
class Log(RawTurtle):
    def __init__(self,canvas,x,y):
        super().__init__(canvas)
        self.shape("images/log.gif")
        self.penup()
        self.goto(x,y)
        
    def forward(self, distance):
        if self.xcor() > 400:
            self.goto(-400,self.ycor())
            
        super().forward(distance)        

class FroggerApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        
    def buildWindow(self):
        self.master.title("Frogger!")
        canvas = tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=tkinter.LEFT)
        
        turtle = RawTurtle(canvas)
        screen = turtle.getscreen()
        screen.tracer(0)
        screen.register_shape("images/frogger.gif")
        screen.register_shape("images/racecar.gif")
        screen.register_shape("images/log.gif")
        
        turtle.color("blue")
        turtle.fillcolor("blue")
        turtle.begin_fill()
        for distance in [350,200,700,200,350]:
            turtle.forward(distance)
            turtle.left(90)
            
        turtle.end_fill()
        turtle.right(90)
        turtle.color("grey")
        turtle.fillcolor("grey")
        turtle.begin_fill()
        for distance in [350,200,700,200,350]:
            turtle.forward(distance)
            turtle.right(90)
            
        turtle.end_fill() 
        turtle.ht()
        
        logs = []
        log = Log(canvas, -500,50)
        logs.append(log)
        
        # -400, 150
        log = Log(canvas, -400,150)
        logs.append(log)        
        
        # -700, 50
        log = Log(canvas, -700,50)
        logs.append(log)         
 
        # -600, 150
        log = Log(canvas, -600,150)
        logs.append(log)         
        
        frog = Frog(canvas)
        
        def jump():
            frog.forward(10)
            screen.update()
            
        screen.onkeypress(jump, "Up")
        
        car = RaceCar(canvas, 500, -50)
        cars = []
        cars.append(car)
        
        # 700, -50
        car = RaceCar(canvas, 700, -50)
        cars.append(car)
        
        # 400, -150
        car = RaceCar(canvas, 400, -150)
        cars.append(car)  
        
        # 600, -150
        car = RaceCar(canvas, 600, -150)
        cars.append(car)         
        
        def animate():
            for car in cars:
                car.forward(2)
                
            for log in logs:
                log.forward(2)
                
            screen.update()
            screen.ontimer(animate, 1)
                
        screen.ontimer(animate)
        
        
        screen.listen()
        
        screen.update()
            
        
        
        
            
        
            
        
    
    
def main():
    root = tkinter.Tk()
    application = FroggerApplication(root)
    application.mainloop()
    
main()
        
        
        