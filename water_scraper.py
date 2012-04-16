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

class WaterScraper(object):
    """Will read the csv, create directories and place the appropriate images in them."""

    def __init__(self, file_name, dest_folder = 'dumps'):
        self._csv_file_name = file_name
        self._destination_folder = dest_folder

    def scrape(self, status_callback = None):
        try:
            water_reader = csv.reader(open(self._csv_file_name, 'rb'))
        except IOError as e:
            return

        if status_callback is not None:
            status_callback('Beginning work on reading {0} into {1}'.format
                            (self._csv_file_name, self._destination_folder))

        column_names = water_reader.next()
        if os.path.isabs(self._destination_folder):
            dump_dir = self._destination_folder
        else:
            dump_dir = os.path.join(os.getcwd(), self._destination_folder)

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
            if status_callback is not None:
                status_string = 'Read line {0}, filter #{1}'.format(water_reader.line_num, row[1])
                status_callback(status_string)

        if status_callback is not None:
            status_callback('Done!')


if __name__ == "__main__":
    scraper = WaterScraper('samples/sample.csv')
    scraper.scrape()
    print 'Done'
