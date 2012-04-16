#!/usr/bin/env python
# coding: utf-8

"""
water_interface is gui front end for water_scraper.
"""
import os
import threading
from Tkinter import *

from water_scraper import WaterScraper

class WaterThread(threading.Thread):
    """Created to allow GUI responsiveness while running the download.

    WaterThread will run a water_scraper operation in it's own thread to allow
    the  WaterInterface GUI to be responsive while the operation is taking place.
    """
    def __init__(self, water_interface):
        """Intitalise the object with an instance of WaterInterface.

        When it is time to run, we'll pass the parameters from the WaterInterface
        to an instance of WaterScraper."""
        self._water_interface = water_interface
        threading.Thread.__init__(self)

    def run(self):
        """Use the current data in our instance of WaterInterface to make
        an instance of a WaterScraper and let it run it's downloads.
        """
        scraper = WaterScraper(self._water_interface.source, self._water_interface.dest)
        scraper.scrape(self._water_interface.status_callback)

class WaterInterface(object):
    """A GUI interface for WaterScraper."""
    def __init__(self, master):
        """Start an instance of WaterInterface

        Keword arguments:
        master -- A reference to an instance of Tk().
        """
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
        """Start the downloading operation.

        Also does a little checking of the input parameters.
        Keyword arguments:
        event -- Passed via Tkinter. Not used.
        """
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

    def log(self, data):
        """Simply posts the data to the long window.

        Keyword arguments:
        data -- Expect this to be a string. Logged to the log text box.
        """
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
        return self.log
    status_callback = property(get_status_callback)


if __name__ == "__main__":
    root = Tk()
    app = WaterInterface(root)
    root.mainloop()
    print 'Done'
