from turtle import *
import tkinter
import math

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
            
        
            
        
    
    
def main():
    root = tkinter.Tk()
    application = FroggerApplication(root)
    application.mainloop()
    
main()
        
        
        