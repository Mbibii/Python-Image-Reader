from PIL import Image
import time

fileLoc = ""
fileLoc = input()

pixelSize = 1

img = ""

# USE C:\Users\chris\source\repos\Python-Image-Reader\images\sprite_test.jpg FOR TESTING

#FUNCTION TO READ PIXELS
def _getPixels(w, h):
    line = ""
    # loop for the width
    for x in range(w):
        # loop for the height
        for y in range(h):
            line = line + ' (' + str(x) + ', ' + str(y) + ') '
        print(line)
        line = "" # resetting string
        time.sleep(1)
        # once line is finished it will go to next row

#---------------------------------------------------------------------#

#MAIN CODE
img = Image.open(fileLoc)
img = img.convert("RGB")
#print(img)
width, height = img.size

_getPixels(width, height)

