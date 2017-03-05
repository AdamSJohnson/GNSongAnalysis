from tkinter import *
"""
def show_entry_fields():
   print("Artist: %s\nTrack: %s" % (e1.get(), e2.get()))
"""

master = Tk()
Label(master, text="Artist").grid(row=0)
Label(master, text="Track").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0)

mainloop()