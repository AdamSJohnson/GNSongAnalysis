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
from tkinter import *

class ComboBoxWindow(Gtk.Window):

    
    def __init__(self):
        self.info = ["","",0,0,0]
        Gtk.Window.__init__(self, title="ComboBox Example")        

        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        #User given artist and track names
        self.artist = Gtk.Entry()
        self.artist.set_placeholder_text("Artist")
        vbox.pack_start(self.artist, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        self.track = Gtk.Entry()
        self.track.set_placeholder_text("Track")
        vbox.pack_start(self.track, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        #Combo boxes have choices, or user data entry
        #Indivual genres are stored and selectable
        genre_store = Gtk.ListStore(str)
        genres = {"Latin":25982, "Blues":36060, "Classical":36061, "World":25984, "Electronica":36055,
            "Country & Western":36059, "Comedy, Spoken & Other":36064, "Traditional Pop":25978,
            "Fold":25971, "Punk":36051, "New Age":36062, "Rock":25964, "Soul/R&B":36057, "Soundtrack":36063, "Reggae":36065,
            "Gospel & Christian":25976, "Children's":25980, "Alternative":25961, "Metal":36053, "Rap/Hip-Hop":36058,
            "Pop":36056, "Dance & House":36054, "Oldies":25965, "Jazz":25974, "Indie":36052}
        for genre in genres:
            genre_store.append([genre])

        genre_combo = Gtk.ComboBox.new_with_model_and_entry(genre_store)
        genre_combo.connect("changed", self.on_genre_combo_changed)
        renderer_text = Gtk.CellRendererText()
        genre_combo.pack_start(renderer_text, True)
        genre_combo.add_attribute(renderer_text, "text", 0)
        vbox.pack_start(genre_combo, False, False, True)

        #Indivual moods are stored and selectable
        mood_store = Gtk.ListStore(str)
        moods = {"Peaceful":65322, "Romantic":65323, "Sentimental":65324, "Tender":42946, "Easygoing":42946,
            "Yearning":65325, "Sophisticated":42954, "Sensual":42947,
            "Cool":65326, "Gritty":65327, "Somber":42948, "Melancholy":42949, "Serious":65328, "Brooding":65329, "Fiery":42953,
            "Urgent":42955, "Defiant":42951, "Aggressive":42958, "Rowdy":65330, "Excited":42960,
            "Energizing":42961, "Energizing":42945, "Stirring":65331, "Lively":65332, "Upbeat":65333}
        for mood in moods:
            mood_store.append([mood])

        mood_combo = Gtk.ComboBox.new_with_model_and_entry(mood_store)
        mood_combo.connect("changed", self.on_mood_combo_changed)
        renderer_text = Gtk.CellRendererText()
        mood_combo.pack_start(renderer_text, True)
        mood_combo.add_attribute(renderer_text, "text", 0)
        vbox.pack_start(mood_combo, False, False, True)

        #Indivual eras are stored and selectable
        era_store = Gtk.ListStore(str)
        eras = {"1930":29490, "1940":29489, "1950":29488, "1960":29487, "1970":29486, "1980":29485, "1990":29484, "2000":29483, "2010":42877}
        for era in eras:
            era_store.append([era])

        era_combo = Gtk.ComboBox.new_with_model_and_entry(era_store)
        era_combo.connect("changed", self.on_era_combo_changed)
        renderer_text = Gtk.CellRendererText()
        era_combo.pack_start(renderer_text, True)
        era_combo.add_attribute(renderer_text, "text", 0)
        vbox.pack_start(era_combo, False, False, True)

        button = Gtk.Button.new_with_label("Submit")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)
        
        self.add(vbox)

    #Called methods when combobox options are chosen
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

    def update_info(self):
        self.info[0] = self.artist.get_text()
        self.info[1] = self.track.get_text()
        for w in self.info
        print w
        #print(self.info[0])
        #print(self.info[1])

    def on_click_me_clicked(self, button):
        self.update_info() 

        


#Display and run
win = ComboBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()