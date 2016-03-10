from turtle import *
import tkinter
import math

def distance(x1,y1,x2,y2):
    a = y1 - y2
    b = x2 - x1
    
    c = math.sqrt(a**2 + b**2)
    return c

def rectangularIntersect(x1,y1,x2,y2):
    if y1 < y2 - 20:
        return False
    
    if y1 > y2 + 20:
        return False
    
    if x1 < x2 - 60:
        return False
    
    if x1 > x2 + 60:
        return False
    
    return True
    

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
        
    def forward(self, dist, frog):
        frogDist = distance(frog.xcor(), frog.ycor(), self.xcor(), self.ycor())
        
        if frogDist < 40:
            self.getscreen().update()
            tkinter.messagebox.showinfo("Ouch", "You ran me over!")
            return False
        
        if self.xcor() < -400:
            self.goto(400,self.ycor())
            
        super().forward(dist)
        return True
      
class Log(RawTurtle):
    def __init__(self,canvas,x,y):
        super().__init__(canvas)
        self.shape("images/log.gif")
        self.penup()
        self.goto(x,y)
        
    def forward(self, distance, frog):
        if rectangularIntersect(self.xcor(), self.ycor(), frog.xcor(), frog.ycor()):
            moveFrog = True
        else:
            moveFrog = False
            
        if self.xcor() > 400:
            self.goto(-400,self.ycor())
            if moveFrog:
                frog.goto(self.xcor(), self.ycor())
            
        if moveFrog:
            frog.right(90)
            frog.forward(distance)
            frog.left(90)
            
        super().forward(distance)  
        
        return moveFrog

class Croc(RawTurtle):
    def __init__(self,canvas,x,y):
        super().__init__(canvas)
        self.shape("images/crock.gif")
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
        
        frame = tkinter.Frame(self)
        frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        scoreVal = tkinter.StringVar()
        scoreVal.set("0")
        scoreTitle = tkinter.Label(frame,text="Score")
        scoreTitle.pack()
        scoreFrame = tkinter.Frame(frame,height=2,bd=1,relief=tkinter.SUNKEN)
        scoreFrame.pack()
        score = tkinter.Label(scoreFrame,height=2,width=20,textvariable=scoreVal,fg="yellow",bg="black")
        score.pack()
        
        livesTitle = tkinter.Label(frame,text="Frog Lives Remaining")
        livesTitle.pack()
        
        livesFrame = tkinter.Frame(frame, height=50,width=60,relief=tkinter.SUNKEN)
        livesFrame.pack()
        livesCanvas = ScrolledCanvas(livesFrame,150,50,150,50)
        livesCanvas.pack()
        
        livesTurtle = RawTurtle(livesCanvas)
        livesScreen = livesTurtle.getscreen()
        livesScreen.tracer(0)
        livesTurtle.ht()
        livesScreen.bgcolor("black")
        livesScreen.register_shape("images/frogger.gif")
        f1 = Frog(livesCanvas)
        f2 = Frog(livesCanvas)
        f3 = Frog(livesCanvas)
        f1.goto(-50,0)
        f2.goto(0,0)
        f3.goto(50,0)
        lives = [f1, f2, f3]
        livesScreen.update()
        self.score = 0
        self.lives = 4
        
        
        
        turtle = RawTurtle(canvas)
        screen = turtle.getscreen()
        screen.tracer(0)
        screen.register_shape("images/frogger.gif")
        screen.register_shape("images/racecar.gif")
        screen.register_shape("images/log.gif")
        screen.register_shape("images/crock.gif")
        
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
            self.score += 10
            scoreVal.set(str(self.score))
            frog.forward(10)
            screen.update()
            
        screen.onkeypress(jump, "Up")
        
        def superJump():
            self.score += 50
            scoreVal.set(str(self.score))
            frog.forward(50)
            screen.update()
            
        screen.onkeypress(superJump, "h")
        
        crocs = []
        
        croc = Croc(canvas, -800, 150)
        crocs.append(croc)
        
        # -900, 50
        croc = Croc(canvas, -900, 50)
        crocs.append(croc)
        
        # 1000, 150
        croc = Croc(canvas, -1000, 150)
        crocs.append(croc)        
        
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
                if not car.forward(2, frog):
                    frog.goto(0,-250)
                    self.lives = self.lives - 1
                    if self.lives == 0:
                        tkinter.messagebox.showinfo("Game Over", "Thanks for playing...")
                        return
                        
                    lives[self.lives-1].ht()  
                    livesScreen.update()
                    
                
            onALog = False
            for log in logs:
                if log.forward(2, frog):
                    onALog = True
                    
            if not onALog and frog.ycor() > 0 and frog.ycor() < 200:
                tkinter.messagebox.showinfo("YumYum", "You just fed the crocodiles...")
                frog.goto(0,-250)
                self.lives = self.lives - 1
                if self.lives == 0:
                    tkinter.messagebox.showinfo("Game Over", "Thanks for playing...")
                    return                
                lives[self.lives-1].ht()
                livesScreen.update()
                
                
            for croc in crocs:
                croc.forward(2)
                
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
        
        
        