from tkinter import *
import tkinter as tk

import phonebook_gui
import phonebook_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(600,350)
        self.master.maxsize(600,350)
        phonebook_func.center_window(self,600,350)
        self.master.title("Phonebook Demo")
        self.master.configure(bg="#dddddd")
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        phonebook_gui.load_gui(self)


if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
            
