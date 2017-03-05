#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk, Image
import time
import os

class Splash(Toplevel):

    '''
    Initialize the splash screen
    '''
    def __init__(self, parent):
        
        Toplevel.__init__(self, parent)

        img = ImageTk.PhotoImage(Image.open("resources/Gracenote_Logo.jpg"))
        panel = Label(parent, image = img)
        panel.pack()

        # needed to make this window show before the program reaches the mainloop
        self.update()

        
class App(Tk):

    '''
    The main program
    '''
    def __init__(self):        
        Tk.__init__(self)
        
        self.withdraw()
        splash = Splash(self)

        # setup stuff goes here
        self.title("Main Window")
        
        # simulate a delay while loading
        time.sleep(10)

        # finished loading so destroy splash
        splash.destroy()

        # show window again
        self.deiconify()

if __name__ == "__main__":
    
    app = App()
    app.mainloop()
