from PIL import Image
import time

# A PROGRAM THAT WILL BE USED TO MAKE 2D UNITY LEVELS
# RIGHT NOW JUST GETS THE FLOORING OF THE LEVEL, WILL MAKE A SEPERATE PROGRAM TO READ THE FILE DATA AND PROBABLY TURN IT INTO A UNITY PREFAB TO DOWNLOAD - IDK ATM

###### KEY ######
# HASHTAGS EQUAL COMMENTS - SHOULDN'T BE READ BY UNITY AS DATA
# DOUBLE DASHES ARE STUFF TO BE READ BY UNITY AS DATA

#---------------------------------------------------------------------#

#USE C:\Users\chris\source\repos\Python-Image-Reader\images\sprite_test.jpg FOR TESTING

#FUNCTION TO BUILD THE STRING FOR THE TEXT FILE
def _buildtextString(array, coordLine):
    string = ""

    for x in range(len(array)):
        string = string + str(array[x]) + " \n"

    #GETS THE COORDS FOR UNITY
    string = string + " \n \n# UNITY COORDS # \n \n"
    string = string + coordLine

    return string

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
            if px[y, x] == (0, 0, 0):
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

    with open("C:\\Users\\chris\\source\\repos\\Python-Image-Reader\\files\\demofile.txt", "w") as filePath:
        _writeToFile(filePath, _buildtextString(lines, coordLine))


#---------------------------------------------------------------------#

#MAIN CODE
fileLoc = input()

img = ""

img = Image.open(fileLoc)
img = img.convert("RGB")

#print(img)
width, height = img.size
px = img.load()

_getPixels(width, height, px)