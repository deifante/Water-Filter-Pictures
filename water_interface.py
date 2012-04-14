#!/usr/bin/env python
# coding: utf-8

"""
water_interface is gui front end for water_scraper.
"""
import os
from Tkinter import *

from water_scraper import WaterScraper

__author__  = "Deifante Jay Walters"
__version__ = "0.1.0"

class WaterInterface(object):

    def __init__(self, master):
        frame = Frame(master)
        self.__master = master
        master.resizable(FALSE,FALSE)
        master.title("Steve's Water App")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        master.bind('<Return>', self.go)

        Label(frame, text='Source (.csv)').grid(column=1, row=1, sticky=(W, E))
        self.__source = Entry(frame, width=40)
        self.__source.grid(column=2, row=1, sticky=(W, E))

        Label(frame, text='Destination (folder)').grid(column=1, row=2, sticky=(W,E))
        self.__dest = Entry(frame, width=40)
        self.__dest.grid(column=2, row=2, sticky=(W,E))

        self.button = Button(frame, text="Go", command=self.go).grid(column=2, row=3, sticky=(W,E))

        for child in frame.winfo_children():
            child.grid_configure()

    def go(self, event = None):
        source = self.__source.get().strip()
        dest = self.__dest.get().strip()

        if len(source) > 0 and len(dest) > 0 and os.path.isfile(source):
            scraper = WaterScraper(source, dest)
            self.update_title('Working...')
            scraper.scrape()
            self.update_title('Done!')

    def update_title(self, new_title):
        if not new_title.startswith("Steve's Water App"):
            new_title = "Steve's Water App - {0}".format(new_title)
        self.__master.title(new_title)

if __name__ == "__main__":
    root = Tk()
    app = WaterInterface(root)
    root.mainloop()
    print 'Done'
