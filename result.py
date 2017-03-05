import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from runthis import __run__
from tkinter import *

class Results(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Results")   


#Display and run
win = ComboBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()