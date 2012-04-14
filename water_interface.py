#!/usr/bin/env python
# coding: utf-8

"""
water_interface is gui front end for water_scraper.
"""
import os
import threading
from Tkinter import *

from water_scraper import WaterScraper

__author__  = "Deifante Jay Walters"
__version__ = "0.2.0"

class WaterThread(threading.Thread):
    def __init__(self, water_interface):
        self.__water_interface = water_interface
        threading.Thread.__init__(self)

    def run(self):
        scraper = WaterScraper(self.__water_interface.source, self.__water_interface.dest)
        scraper.scrape(self.__water_interface.status_callback)

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

        Button(frame, text="Go", command=self.go).grid(column=2, row=3, sticky=(W,E))

        Label(frame, text='Log').grid(column=1, row=4, sticky=(W,E))
        self.__logging_window = Text(frame, width=40)
        self.__logging_window.config(state=DISABLED)
        self.__logging_window.grid(column=2, row=4, sticky=(W,E))

        for child in frame.winfo_children():
            child.grid_configure()

    def go(self, event = None):
        source = self.__source.get().strip()
        dest = self.__dest.get().strip()

        if len(source) <= 0 or not os.path.isfile(source):
            self.log('Invalid Source')
            return

        if len(dest) <= 0:
            self.log('Invalid Destination')
            return

        scraper = WaterScraper(source, dest)
        water_thread = WaterThread(self)
        water_thread.start()

    def update_title(self, new_title):
        if not new_title.startswith("Steve's Water App"):
            new_title = "Steve's Water App - {0}".format(new_title)
        self.__master.title(new_title)

    def status_update_callback(self, new_status):
        self.log(new_status)

    def log(self, data):
        self.__logging_window.config(state=NORMAL)
        self.__logging_window.insert(END, data + '\n')
        self.__logging_window.config(state=DISABLED)

    def get_source(self):
        return self.__source.get().strip()
    source = property(get_source)

    def get_dest(self):
        return self.__dest.get().strip()
    dest = property(get_dest)

    def get_status_callback(self):
        return self.status_update_callback
    status_callback = property(get_status_callback)

if __name__ == "__main__":
    root = Tk()
    app = WaterInterface(root)
    root.mainloop()
    print 'Done'
