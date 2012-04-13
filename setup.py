#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup

# The target platform is Windows and the dev platform is linux
try:
    import py2exe
except ImportError:
    pass

setup(name         = 'Water Filter Pictures',
      author       = 'Deifante Jay Walters',
      author_email = 'deifante@gmail.com',
      description  = 'Uses csv input to organise and download a set of jpgs.',
      py_modules   = ['water_interface', 'water_scraper'],
      requires     = ['Tkinter', 'csv', 'urllib', 'os'],
      version      = '0.2',
      provides     = ['water_scraper', 'water_interface'],
      url          = 'http://www.deifante.com/',
      # Used by py2exe to create a gui executable for windows.
      windows      = ['water_interface.py']
      )
