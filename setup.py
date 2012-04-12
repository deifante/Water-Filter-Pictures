from distutils.core import setup
#import py2exe

setup(name         = 'Water Filter Pictures',
      author       = 'Deifante Jay Walters',
      author_email = 'deifante@gmail.com',
      description  = 'Uses csv input to organise and download a set of jpgs.',
      py_modules   = ['water_interface', 'water_scraper'],
      requires     = ['Tkinter', 'csv', 'urllib', 'os'],
      version      = '0.1',
      provides     = ['water_scraper', 'water_interface'],
      url          = 'http://www.deifante.com/'
      )
