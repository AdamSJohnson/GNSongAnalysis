#!/usr/bin/python3

from tkinter import *
import time

class App():

    '''
    The main program
    '''
    def __init__(self):        
        
        top = Tk()

        # setup stuff goes here
        top.title("Main Window")

        top.geometry("500x500")

        tkvarGenre = StringVar(top)
        tkvarMood = StringVar(top)
        tkvarEra = StringVar(top)

        genreChoices = {25982:'Latin', } # a dictionary (map) of ID's and Genres respectively (ID:Genre)
        moodChoices = {} 
        eraChoices = {}

        tkvar.set('Latin') # Sets init val of drop down menu
        genreOptionMenu = OptionMenu(top, tkvarGenre, list(genreChoices.values()))

        tkvar.set('')
        moodOptionMenu = OptionMenu(top, tkvarMood, list(moodChoices.values()))

        tkvar.set('')
        eraChoices = OptionMenu(top, tkvarEra, list(eraChoices.values()))

        genreOptionMenu.pack(fill="none", expand = True)
        moodOptionMenu.pack(fill="none", expand = True)
        eraChoices.pack(fill="none", expand = True)
        
        B = Button(top, text = "Run")
        B.pack(fill="none", expand = True)

        top.mainloop()

if __name__ == "__main__":
    
    app = App()
