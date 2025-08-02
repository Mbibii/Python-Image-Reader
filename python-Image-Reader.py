from PIL import Image
import time

fileLoc = input()

img = ""

# USE C:\Users\chris\source\repos\Python-Image-Reader\images\sprite_test.jpg FOR TESTING

#FUNCTION TO OUTPUT TO FILE - DOESN'T WORK FULLY ATM
def _writeToFile(file, text):
    file.write(text)


#FUNCTION TO READ PIXELS
def _getPixels(w, h, px):

    line = ""

    # loop for the width
    for x in range(h):
        line = line + "# "
        # loop for the height
        for y in range(w):
            
            #line = line + ' (' + str(x) + ', ' + str(y) + ') '
            if px[y, x] == (0, 0, 0):
                line = line + " 1 "
            else:
                line = line + "   "

        line = line + " #"
        print(line)
        
        with open("C:\\Users\\chris\\source\\repos\\Python-Image-Reader\\files\\demofile.txt", "w") as filePath:
            _writeToFile(filePath, line)

        line = "" # resetting string    
        time.sleep(0.1)
        # once line is finished it will go to next row


#---------------------------------------------------------------------#

#MAIN CODE
img = Image.open(fileLoc)
img = img.convert("RGB")

#print(img)
width, height = img.size
px = img.load()

_getPixels(width, height, px)

