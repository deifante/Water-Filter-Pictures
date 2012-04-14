# Overview
Provide a simple app to download and orgainse pictures for a water filter NGO in Cambodia.

Water Filter Pictures provides 2 small Python classes. The main functionality is to take input of a csv detailing a a Village, Filter and URL. The URL points to a jpg that will be saved in a folder named after the village. The jpg will be renamed to match the name of the filter that is on the same row. All the pictures from the same village will end up in the same folder.

## Usage
### Windows (without Python interpreter installed)
1. Unpack the archive for your [Water-Filter-Pictures-bin-win32-0.1.zip](https://github.com/downloads/deifante/Water-Filter-Pictures/Water-Filter-Pictures-bin-win32-0.1.zip).
2. Double click the file named water_interface.exe
3. Provide the the full or relative path to the source csv in the top input box labeled "Source".
4. Provide the full or relative path to the folder where you'd like the images to be placed in the input box labeled "Destination".
5. Press the button labeled go.
6. When the log text box has a line ending in "Done!", the operation is complete.

### *nix
1. Download project from the [Downloads page](https://github.com/deifante/Water-Filter-Pictures/downloads).
2. Unpack appropriate archive file.
3. > python water_interface.py
4. Provide the the full or relative path to the source csv in the top input box labeled "Source".
5. Provide the full or relative path to the folder where you'd like the images to be placed in the input box labeled "Destination".
6. Press the button labeled go.
7. When the log text box has a line ending in "Done!", the operation is complete.