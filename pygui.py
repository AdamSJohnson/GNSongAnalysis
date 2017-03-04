#!/usr/bin/python3

#Code from http://stackoverflow.com/questions/21253148/multiple-line-comment-in-python

import tkinter as tk
import time

class Splash(tk.Toplevel):

    '''
    Initialize the splash screen
    '''
    def __init__(self, parent):
        
        tk.Toplevel.__init__(self, parent)

        # needed to make window show before the program reaches the mainloop
        self.update()

        
class App(tk.Tk):

    '''
    The main program
    '''
    def __init__(self):
        
        tk.Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)

        ## setup stuff goes here
        self.title("Main Window")
        
        ## simulate a delay while loading
        time.sleep(6)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()

if __name__ == "__main__":
    
    app = App()
    app.mainloop()
