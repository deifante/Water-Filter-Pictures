#!/usr/bin/env python
# coding: utf-8

"""
water_scraper is a Python library for reading a specified csv file.
The csv file contains a Village, filter and image url. This class
will retrieve the image name it after it's filter #  and put it in
a directory for it's village.
"""
import os
import csv
import urllib

__author__  = "Deifante Jay Walters"
__version__ = "0.1.0"

class WaterScraper(object):
    """Will read the csv, create directories and place the appropriate images in them."""

    def __init__(self, file_name, dest_folder = 'dumps'):
        self.__csv_file_name = file_name
        self.__destination_folder = dest_folder

    def scrape(self):
        try:
            water_reader = csv.reader(open(self.__csv_file_name, 'rb'))
        except IOError as e:
            return

        column_names = water_reader.next()
        if os.path.isabs(self.__destination_folder):
            dump_dir = self.__destination_folder
        else:
            dump_dir = os.path.join(os.getcwd(), self.__destination_folder)

        created_directories = {}
        for row in water_reader:
            if row[0] not in created_directories:
                if len(row[0]) == 0:
                    new_directory = os.path.join(dump_dir, 'Unknown Village')
                else:
                    new_directory = os.path.join(dump_dir, row[0])
                created_directories[row[0]] = new_directory
                if not os.path.exists(new_directory):
                    os.makedirs(new_directory)

            # Because the file extensions end in /.jpg it takes a little more
            # work than usual to get the file extension.
            extension = row[2][-3:]
            if extension != 'jpg' and len(os.path.splitext(row[2])):
                extension = os.path.splitext(row[2])

            new_filename = "{0}.{1}".format(row[1], extension)
            urllib.urlretrieve(row[2], os.path.join(created_directories[row[0]],new_filename))

if __name__ == "__main__":
    scraper = WaterScraper('samples/sample.csv')
    scraper.scrape()
    print 'Done'
