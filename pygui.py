"""#!/usr/bin/python3

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
        

        genreChoices = {25982:'Latin', } # a dictionary (map) of ID's and Genres respectively (ID:Genre)
        moodChoices = {} 
        eraChoices = {}

        tkvarGenre = StringVar(top)
        tkvarGenre.set('Latin') # Sets init val of drop down menu
        genreOptionMenu = OptionMenu(top, tkvarGenre, list(genreChoices.values()))

        tkvarMood = StringVar(top)
        tkvarMood.set('Happy')
        moodOptionMenu = OptionMenu(top, tkvarMood, list(moodChoices.values()))

        tkvarera = StringVar(top)
        tkvarera.set('90\'s')
        eraChoices = OptionMenu(top, tkvarera, list(eraChoices.values()))

        genreOptionMenu.pack(fill="none", expand = True)
        moodOptionMenu.pack(fill="none", expand = True)
        eraChoices.pack(fill="none", expand = True)
        
        B = Button(top, text = "Run")
        B.pack(fill="none", expand = True)

        top.mainloop()

if __name__ == "__main__":
    
    app = App()
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ComboBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ComboBox Example")

        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        genre_store = Gtk.ListStore(str)
        genres = {"Austria", "Brazil", "Belgium", "France", "Germany",
            "Switzerland", "United Kingdom", "United States of America",
            "Uruguay"}
        for genre in genres:
            genre_store.append([genre])

        genre_combo = Gtk.ComboBox.new_with_model_and_entry(genre_store)
        genre_combo.connect("changed", self.on_genre_combo_changed)
        renderer_text = Gtk.CellRendererText()
        genre_combo.pack_start(renderer_text, True)
        genre_combo.add_attribute(renderer_text, "text", 0)
        vbox.pack_start(genre_combo, False, False, True)

        mood_store = Gtk.ListStore(str)
        moods = ["Austria", "Brazil", "Belgium", "France", "Germany",
            "Switzerland", "United Kingdom", "United States of America",
            "Uruguay"]
        for mood in moods:
            mood_store.append([mood])

        mood_combo = Gtk.ComboBox.new_with_model_and_entry(mood_store)
        mood_combo.connect("changed", self.on_mood_combo_changed)
        renderer_text = Gtk.CellRendererText()
        mood_combo.pack_start(renderer_text, True)
        mood_combo.add_attribute(renderer_text, "text", 0)
        vbox.pack_start(mood_combo, False, False, True)

        era_store = Gtk.ListStore(str)
        eras = ["Austria", "Brazil", "Belgium", "France", "Germany",
            "Switzerland", "United Kingdom", "United States of America",
            "Uruguay"]
        for era in eras:
            era_store.append([era])

        era_combo = Gtk.ComboBox.new_with_model_and_entry(era_store)
        era_combo.connect("changed", self.on_era_combo_changed)
        renderer_text = Gtk.CellRendererText()
        era_combo.pack_start(renderer_text, True)
        era_combo.add_attribute(renderer_text, "text", 0)
        vbox.pack_start(era_combo, False, False, True)

        self.add(vbox)

    def on_genre_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            genre = model[tree_iter][0]
            print("Selected: genre=%s" % genre)

    def on_mood_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            mood = model[tree_iter][0]
            print("Selected: mood=%s" % mood)

    def on_era_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            era = model[tree_iter][0]
            print("Selected: era=%s" % era)

win = ComboBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
