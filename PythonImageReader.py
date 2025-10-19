from PIL import Image
import time


# A PROGRAM THAT WILL BE USED TO MAKE 2D UNITY LEVELS
# RIGHT NOW JUST GETS THE FLOORING OF THE LEVEL, WILL MAKE A SEPERATE PROGRAM TO READ THE FILE DATA AND PROBABLY TURN IT INTO A UNITY PREFAB TO DOWNLOAD - IDK ATM

###### KEY ######
# HASHTAGS EQUAL COMMENTS - SHOULDN'T BE READ BY UNITY AS DATA
# DOUBLE DASHES ARE STUFF TO BE READ BY UNITY AS DATA

#---------------------------------------------------------------------#

#USE C:\Users\chris\source\repos\Python-Image-Reader\images\sprite_test.jpg FOR TESTING     [12 x 12]
#USE C:\Users\chris\source\repos\Python-Image-Reader\images\sprite_test_2.jpg FOR TESTING   [32 x 32]

#---------------------------------------------------------------------#


class FileLocations:
    #filename = "python-image-reader-text-file.txt"
    #outputFile = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + "\\" + filename     #defaults to desktop
    outputFile = "C:\\Users\\chris\\source\\repos\\Python-Image-Reader\\files\\demofile.txt"
    inputFile = ""

class Colors:
    floor = (0, 0, 0)
    wall = (255, 0, 0) # not used
    nothing = (255, 255, 255) 
    spawn = (0, 255, 0) # not used


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

    time.sleep(1000)

def _blackPixel_Threshold(pixelCol):

    # THIS FUNCTION WILL BE USED TO GET A THRESHOLD FOR THE BLACK PIXELS SO THEN IT'S A LOT MORE DYNAMIC

    THRESH = 80
    LIGHT_THRESH = 110
    LIGHTER_THRESH = 140
    LIGHTERER_THRESH = 180

    r = pixelCol[0]
    g = pixelCol[1]
    b = pixelCol[2]

    r_base = Colors.floor[0]
    g_base = Colors.floor[1]
    b_base = Colors.floor[2]

    if abs(r_base - r) > THRESH or abs(g_base - g) > THRESH or abs(b_base - b) > THRESH:
        if abs(r_base - r) < LIGHT_THRESH or abs(g_base - g) < LIGHT_THRESH or abs(b_base - b) < LIGHT_THRESH:
            return 1
        elif abs(r_base - r) < LIGHTER_THRESH or abs(g_base - g) < LIGHTER_THRESH or abs(b_base - b) < LIGHTER_THRESH:
            return 4
        elif abs(r_base - r) < LIGHTERER_THRESH or abs(g_base - g) < LIGHTERER_THRESH or abs(b_base - b) < LIGHTERER_THRESH:
            return 5
        else:
            return 0
    else:
        return 2
    
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
            #if px[y, x] == Colors.floor and (px[y - 1, x] == Colors.nothing or px[y + 1, x] == Colors.nothing 
                                             #or px[y, x - 1] == Colors.nothing or px[y, x + 1] == Colors.nothing):
            # kojima fix
            if _blackPixel_Threshold(px[y, x]) == 2: #black
                line = line + " . "
            elif _blackPixel_Threshold(px[y, x]) == 1: #slightly black
                line = line + " ~ "
            elif _blackPixel_Threshold(px[y, x]) == 4:
                line = line + " # "
            elif _blackPixel_Threshold(px[y, x]) == 5:
                line = line + " [ "
            else:
                line = line + " 1 "
            coordLine = coordLine + "-- Vector2(" + str(x) + ", " + str(y) + ") " + " \n"
        line = line + " #"
        lines[y] = line
        print(line)
        line = "" # resetting string    
        time.sleep(0.1)
        # once line is finished it will go to next row
    with open(FileLocations.outputFile, "w") as filePath:
        _writeToFile(filePath, _buildtextString(lines, coordLine))

#---------------------------------------------------------------------#

class BasicCommands():
    def _start():
        print("-------------------------------------")
        print("please enter file to read: ")
        FileLocations.inputFile = input()

        img = ""

        img = Image.open(FileLocations.inputFile)
        img = img.convert("RGB")

        #print(img)
        width, height = img.size
        px = img.load()

        if width > 32 or height > 32:
            print("file too big - needs to be at most 32x32")
        else:
            _getPixels(width, height, px)

#-----------------------------C----------------------------------------#

class Main():
    def _Main():
        print("-------------------------------------")
        print("# IMAGE FILE READER FOR UNITY LEVEL #")
        print("-------------------------------------")
        print("Actions you can take:")
        print("1 - Start Program")
        print("4 - Exit Program")

        if input() == "1":
            BasicCommands._start()
        elif input() == "4":
            exit()
        else:
            "Invalid Input"

Main._Main()