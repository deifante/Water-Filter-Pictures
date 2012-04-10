#!/usr/bin/env python
# coding: utf-8

"""
water_scraper is a Python library for reading a specified csv file, then creating directories
for the related images.
"""
import os
import csv
import urllib

__author__ = "Deifante Jay Walters"
__version__ = "0.0.1"

class WaterScraper(object):
    """Will read the scv, create directories and place the appropriate images in them."""

    def __init__(self, file_name):
        self.__csv_file_name = file_name
        self.__destination_folder = 'dest'

    def scrape(self):
        water_reader = csv.reader(open(self.__csv_file_name, 'rb'))
        column_names = water_reader.next()
        dump_dir = os.path.join(os.getcwd(), 'dumps')
        
        created_directories = {}
        for row in water_reader:
            if row[0] not in created_directories:
                new_directory = os.path.join(dump_dir, row[0])
                created_directories[row[0]] = new_directory
                os.makedirs(new_directory)
        
            extension = row[2][-3:]
            if extension != 'jpg' and len(os.path.splitext(row[2])):
                extension = os.path.splitext(row[2])
                
            new_filename = "{0}.{1}".format(row[1], extension)
            urllib.urlretrieve(row[2], os.path.join(created_directories[row[0]],new_filename))

if __name__ == "__main__":
    scraper = WaterScraper('samples/sample.csv')
    scraper.scrape()
    print 'Done'
