#!/usr/bin/env python
from Tkinter import *


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        #<create the rest of your GUI here>

if __name__ == "__main__":
    root = Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
