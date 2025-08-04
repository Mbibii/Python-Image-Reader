from PIL import Image
import time
import PythonImageReader as pir
import Data

#FUNCTION TO OUTPUT TO FILE - DOESN'T WORK FULLY ATM
def _writeToFile(file, text):
    file.write(text)
    print("added : " + str(text) + " to file : " + str(file))
#FUNCTION TO READ PIXELS

def _getPixels(w, h, px):
    lines = [None] * w    # need enough places for all the data
    line = ""
    coordLine = ""
    # loop for the width
    for x in range(h):
        line = line + "# "
        # loop for the height
        for y in range(w):
            #line = line + ' (' + str(x) + ', ' + str(y) + ') '
            if px[y, x] == Data.Colors.floor and (px[y - 1, x] == Data.Colors.nothing or px[y + 1, x] == Data.Colors.nothing 
                                             or px[y, x - 1] == Data.Colors.nothing or px[y, x + 1] == Data.Colors.nothing):
                line = line + " 1 "
                coordLine = coordLine + "-- Vector2(" + str(x) + ", " + str(y) + ") " + " \n" 
            else:
                line = line + "   "
        line = line + " #"
        lines[x] = line
        print(line)
        line = "" # resetting string    
        time.sleep(0.1)
        # once line is finished it will go to next row
    with open(Data.FileLocations.outputFile, "w") as filePath:
        _writeToFile(filePath, pir._buildtextString(lines, coordLine))