#!/usr/bin/env python
# coding: utf-8

"""
water_interface is gui front end for water_scraper.
"""
from Tkinter import *

from water_scraper import WaterScraper

__author__  = "Deifante Jay Walters"
__version__ = "0.0.1"

class WaterInterface(object):

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        Label(frame, text='Source (.csv)').pack(side=LEFT)
        self.__source = Text(frame, height=1)
        self.__source.pack(side=LEFT)

        Label(frame, text='Destination (folder)').pack(side=LEFT)
        self.__dest = Text(frame, height=1)
        self.__dest.pack(side=LEFT)

        self.button = Button(frame, text="Go", command=self.go)
        self.button.pack(side=RIGHT)

    def go(self):
        source = self.__source.get(1.0, END).strip()
        dest = self.__dest.get(1.0, END).strip()

        if len(source) > 0 and len(dest) > 0:
            scraper = WaterScraper(source, dest)
            scraper.scrape()


if __name__ == "__main__":
    root = Tk()
    app = WaterInterface(root)
    root.mainloop()
    print 'Done'
