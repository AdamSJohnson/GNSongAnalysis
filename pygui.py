import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from runthis import __run__
from tkinter import *

class ComboBoxWindow(Gtk.Window):

    
    def __init__(self):
        self.info = ["","","0","0","0"]
        Gtk.Window.__init__(self, title="Analyze")        

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
        self.genres = {"Latin":'25982', "Blues":'36060', "Classical":'36061', "World":'25984', "Electronica":'36055',
            "Country & Western":'36059', "Comedy, Spoken & Other":'36064', "Traditional Pop":'25978',
            "Fold":'25971', "Punk":'36051', "New Age":'36062', "Rock":'25964', "Soul/R&B":'36057', "Soundtrack":'36063', "Reggae":'36065',
            "Gospel & Christian":'25976', "Children's":'25980', "Alternative":'25961', "Metal":'36053', "Rap/Hip-Hop":'36058',
            "Pop":'36056', "Dance & House":'36054', "Oldies":'25965', "Jazz":'25974', "Indie":'36052'}
        #for genre in self.genres:
         #   genre_store.append([genre])
            
        genre_combo = Gtk.ComboBoxText()
        #genre_combo = Gtk.ComboBox.new_with_model_and_entry(genre_store)
        genre_combo.connect("changed", self.on_genre_combo_changed)
        #renderer_text = Gtk.CellRendererText()
        #genre_combo.pack_start(renderer_text, True)
        #genre_combo.add_attribute(renderer_text, "text", 0)
        for genre in self.genres:
            genre_combo.append_text(genre)
        
        vbox.pack_start(genre_combo, False, False, True)

        #Indivual moods are stored and selectable
        mood_store = Gtk.ListStore(str)
        self.moods = {"Peaceful":'65322', "Romantic":'65323', "Sentimental":'65324', "Tender":'42946', "Easygoing":'42946',
            "Yearning":'65325', "Sophisticated":'42954', "Sensual":'42947',
            "Cool":'65326', "Gritty":'65327', "Somber":'42948', "Melancholy":'42949', "Serious":'65328', "Brooding":'65329', "Fiery":'42953',
            "Urgent":'42955', "Defiant":'42951', "Aggressive":'42958', "Rowdy":'65330', "Excited":'42960',
            "Energizing":'42961', "Energizing":'42945', "Stirring":'65331', "Lively":'65332', "Upbeat":'65333'}
        #for mood in self.moods:
          #  mood_store.append([mood])

        mood_combo = Gtk.ComboBoxText()
        #mood_combo = Gtk.ComboBox.new_with_model_and_entry(mood_store)
        mood_combo.connect("changed", self.on_mood_combo_changed)
        #renderer_text = Gtk.CellRendererText()
        #mood_combo.pack_start(renderer_text, True)
        #mood_combo.add_attribute(renderer_text, "text", 0)
        for mood in self.moods:
            mood_combo.append_text(mood)
            
        vbox.pack_start(mood_combo, False, False, True)

        #Indivual eras are stored and selectable
        era_store = Gtk.ListStore(str)
        self.eras = {"1930":'29490', "1940":'29489', "1950":'29488', "1960":'29487', "1970":'29486', "1980":'29485', "1990":'29484', "2000":'29483', "2010":'42877'}
        #for era in self.eras:
        #    era_store.append([era])


        era_combo = Gtk.ComboBoxText()
        #era_combo = Gtk.ComboBox.new_with_model_and_entry(era_store)
        era_combo.connect("changed", self.on_era_combo_changed)
        #renderer_text = Gtk.CellRendererText()
        #era_combo.pack_start(renderer_text, True)
        #era_combo.add_attribute(renderer_text, "text", 0)
        for era in self.eras:
            era_combo.append_text(era)
        
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
            self.info[2] = self.genres[genre]
            #print("Selected: genre=%s" % genre)


    def on_mood_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            mood = model[tree_iter][0]
            self.info[3] = self.moods[mood]
            #print("Selected: mood=%s" % mood)

    def on_era_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            era = model[tree_iter][0]
            self.info[4] = self.eras[era]
            #print("Selected: era=%s" % era)

    def update_info(self):
        self.info[0] = self.artist.get_text()
        self.info[1] = self.track.get_text()
        for w in self.info:
            print(w)        

    def on_click_me_clicked(self, button):
        self.update_info() 
        results = __run__().run(self.info)
        print(results)
        s=self.ExitScreen(results)

    def ExitScreen(self, results):
        

        self.set_default_size(1000,1000)
        Gtk.Window.__init__(self, title="Results")

        grid = Gtk.Grid()
        self.add(grid)

        for key in results:

            button2 = Gtk.Button(label= key + str(results[key][0][0]))
            #button3 = Gtk.Button(label="Button 3")
        


        grid.add(button2)
        grid.attach(button2, 1, 0, 2, 1)
        #grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        #grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        #grid.attach(button5, 1, 2, 1, 1)
        #grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

        


#Display and run
win = ComboBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
