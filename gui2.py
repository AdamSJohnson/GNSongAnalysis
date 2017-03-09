import tkinter as tk
from runthis import __run__ as rt


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

        # add a mood option menu
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
        rt.run(self,_list=send)
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    Demo1(root)
    root.mainloop()
