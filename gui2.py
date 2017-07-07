import tkinter as tk
from runthis import __run__ as rt
from tkinter import END, LEFT, RIGHT, TOP, BOTTOM, BOTH, Y, NE, NS, NSEW, W, E, YES
from tkinter import ttk
from tkinter.font import Font
from tkinter import VERTICAL, HORIZONTAL
import random
import spotipy
import json
spotify = spotipy.Spotify()

class Demo1:
    def __init__(self, master):
        #our genre lookup
        self.genres = {"Latin": '25982', "Blues": '36060', "Classical": '36061', "World": '25984',
                       "Electronica": '36055',
                       "Country & Western": '36059', "Comedy, Spoken & Other": '36064', "Traditional Pop": '25978',
                       "Fold": '25971', "Punk": '36051', "New Age": '36062', "Rock": '25964', "Soul/R&B": '36057',
                       "Soundtrack": '36063', "Reggae": '36065',
                       "Gospel & Christian": '25976', "Children's": '25980', "Alternative": '25961', "Metal": '36053',
                       "Rap/Hip-Hop": '36058',
                       "Pop": '36056', "Dance & House": '36054', "Oldies": '25965', "Jazz": '25974', "Indie": '36052'}
        #create our tuple for later
        self.genre_tuple = ['None']
        for x in self.genres:
            self.genre_tuple.append(x)


        #our mood lookup
        self.moods = {"Peaceful": '65322', "Romantic": '65323', "Sentimental": '65324', "Tender": '42946',
                      "Easygoing": '42946',
                      "Yearning": '65325', "Sophisticated": '42954', "Sensual": '42947',
                      "Cool": '65326', "Gritty": '65327', "Somber": '42948', "Melancholy": '42949', "Serious": '65328',
                      "Brooding": '65329', "Fiery": '42953',
                      "Urgent": '42955', "Defiant": '42951', "Aggressive": '42958', "Rowdy": '65330',
                      "Excited": '42960',
                      "Energizing": '42961', "Energizing": '42945', "Stirring": '65331', "Lively": '65332',
                      "Upbeat": '65333'}

        # create our tuple for later
        self.mood_tuple = ['None']
        for x in self.moods:
            self.mood_tuple.append(x)

        #our era lookup
        self.eras = {"1930": '29490', "1940": '29489', "1950": '29488', "1960": '29487', "1970": '29486',
                     "1980": '29485', "1990": '29484', "2000": '29483', "2010": '42877'}

        # create our tuple for later
        self.era_tuple = ['None']
        for x in self.eras:
            self.era_tuple.append(x)

        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Run Analysis', width = 25, command = self.new_window)
        self.button1.pack()

        self.button2 = tk.Button(self.frame, text='Randomize', width=25, command=self.randomize)
        self.button2.pack()

        self.button3 = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.button3.pack()

        #add a entry for our Artist with a label
        self.a_label = tk.Label(self.master, text="Artist").pack()
        self.artist = tk.Entry(self.master,  width = 25)
        self.artist.pack()

        #add a entry for our song with a label
        self.s_label = tk.Label(self.master, text="Song").pack()
        self.song = tk.Entry(self.master, width=25)
        self.song.pack()

        #add a genre option menu
        self.genre_var = tk.StringVar(master)
        self.genre_var.set(self.genre_tuple[0])  # default value
        self.genre_menu = tk.OptionMenu(master, self.genre_var, * self.genre_tuple)
        self.genre_menu.pack()

        # add a mood option menu
        self.mood_var = tk.StringVar(master)
        self.mood_var.set(self.genre_tuple[0])  # default value
        self.mood_menu = tk.OptionMenu(master, self.mood_var, *self.mood_tuple)
        self.mood_menu.pack()

        # add a era option menu
        self.era_var = tk.StringVar(master)
        self.era_var.set(self.genre_tuple[0])  # default value
        self.era_menu = tk.OptionMenu(master, self.era_var, *sorted(self.era_tuple))
        self.era_menu.pack()

        #pack up the frame and move on
        self.frame.pack()

    def new_window(self):
        #artist, title, genre, mood, era
        send = []

        #add on our collected artist
        send.append(self.artist.get())

        #add on our collected song
        send.append(self.song.get())

        #check our genre and add in the lookup
        if self.genre_var.get()  == 'None':
            send.append('')
        else:
            send.append(self.genres[self.genre_var.get()])

        # check our mood and add in the lookup
        if self.mood_var.get() == 'None':
            send.append('')
        else:
            send.append(self.moods[self.mood_var.get()])

        # check our era and add in the lookup
        if self.era_var.get() == 'None':
            send.append('')
        else:
            send.append(self.eras[self.era_var.get()])


        print(send)

        self.intensities = rt.run(self,_list=send)
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow,intensities=self.intensities )

    def randomize(self):
        self.era_var.set(random.choice(self.era_tuple))
        self.mood_var.set(random.choice(self.mood_tuple))
        self.genre_var.set(random.choice(self.genre_tuple))

    def close_windows(self):
        self.master.destroy()

class Demo2:
    SortDir = True
    def __init__(self, master, intensities=''):
        self.master = master
        self.frame = tk.Frame( self.master )
        self.tree_frame = tk.Frame(self.frame, height=400, width=900)
        self.tree_frame.pack_propagate(0)
        self.tree_frame.pack()
        self.dataCols = ('Title', 'Compound',  'Negative', 'Neutral', 'Positive', 'Artist', 'Sample')
        self.tree = ttk.Treeview( self.tree_frame, height = 14, columns= self.dataCols, \
                                      selectmode="extended", show='headings')

        for x in self.dataCols:
            self.data = self.intensity_fixer( intensities=intensities)



        self.tree.pack(fill=BOTH)
        self._load_data()
        self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack(side=LEFT)

        self.exportButton = tk.Button(self.frame, text='Export', width=25, command=self.export_data)


        self.exportButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def export_data(self):
        file_obj = open('export.txt', 'w')
        for item in self.data:
            for x in item:
                file_obj.write(x + " ")
            file_obj.write('\r\n')


    def intensity_fixer(self, intensities=''):
        #[songname, comp, neg, neu, pos, art, sample]
        result =[]
        for item in intensities:
            temp = []
            temp.append(item)
            temp.append('{:05.2f}'.format( 100 * intensities[item][0][0]))
            temp.append('{:05.2f}'.format((100 * intensities[item][0][1])))
            temp.append('{:05.2f}'.format(100 * intensities[item][0][2]))
            temp.append('{:05.2f}'.format(100 * intensities[item][0][3]))
            temp.append('{:30.30}'.format( intensities[item][1]))
            list = self.link(item=item, item2=intensities[item][1])
            if list is None:
                list = ''
            temp.append(list)
            result.append(temp)

        return result

    def _load_data(self):
        # configure column headings
        for c in self.dataCols:
            self.tree.heading(c, text=c.title(),
                              command=lambda c=c: self._column_sort(c, Demo2.SortDir))
            self.tree.column(c, width=Font().measure(c.title()))

        # add data to the tree
        for item in self.data:
            self.tree.insert('', 'end', values=item)


    def _column_sort(self, col, descending=False):

        # grab values to sort as a list of tuples (column value, column id)
        # e.g. [('Argentina', 'I001'), ('Australia', 'I002'), ('Brazil', 'I003')]
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]

        # reorder data
        # tkinter looks after moving other items in
        # the same row
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.tree.move(item[1], '', indx)  # item[1] = item Identifier
            # and adjust column widths if necessary
            for idx, val in enumerate(item):
                iwidth =  Font().measure(val)
                if self.tree.column(self.dataCols[idx], 'width') < iwidth:
                    self.tree.column(self.dataCols[idx], width=iwidth)

        # reverse sort direction for next sort operation
        Demo2.SortDir = not descending
    def link(self, item='', item2=''):
        return 'no link'
''' This is broken right now
    def link(self, item='', item2=''):
        if not item:
            return 'no link'
        try:
            results = spotify.search(q='artist:' + item2 + ' track:' + item, type='track')
        except json.decoder.JSONDecodeError:
            return 'No link found'
        items = results['tracks']['items']
        if len(items) > 0:
            artist = items[0]
            return artist['preview_url']
'''
if __name__ == "__main__":
    root = tk.Tk()
    Demo1(root)
    root.mainloop()
