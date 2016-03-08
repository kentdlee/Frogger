from turtle import *
import tkinter
import math

class FroggerApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        
    def buildWindow(self):
        pass
    
    
def main():
    root = tkinter.Tk()
    application = FroggerApplication(root)
    application.mainloop()
    
main()
        
        
        