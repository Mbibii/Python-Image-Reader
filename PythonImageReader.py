from PIL import Image
import FileReader as fr
import Data as Data


# A PROGRAM THAT WILL BE USED TO MAKE 2D UNITY LEVELS
# RIGHT NOW JUST GETS THE FLOORING OF THE LEVEL, WILL MAKE A SEPERATE PROGRAM TO READ THE FILE DATA AND PROBABLY TURN IT INTO A UNITY PREFAB TO DOWNLOAD - IDK ATM

###### KEY ######
# HASHTAGS EQUAL COMMENTS - SHOULDN'T BE READ BY UNITY AS DATA
# DOUBLE DASHES ARE STUFF TO BE READ BY UNITY AS DATA

#---------------------------------------------------------------------#

#USE C:\Users\chris\source\repos\Python-Image-Reader\images\sprite_test.jpg FOR TESTING     [12 x 12]
#USE C:\Users\chris\source\repos\Python-Image-Reader\images\sprite_test_2.jpg FOR TESTING   [32 x 32]

#---------------------------------------------------------------------#

#FUNCTION TO BUILD THE STRING FOR THE TEXT FILE
def _buildtextString(array, coordLine):
    string = ""

    for x in range(len(array)):
        string = string + str(array[x]) + " \n"

    #GETS THE COORDS FOR UNITY
    string = string + " \n \n# UNITY COORDS # \n \n"
    string = string + coordLine

    return string

#---------------------------------------------------------------------#

class BasicCommands():
    def _start():
        print("-------------------------------------")
        print("please enter file to read: ")
        Data.FileLocations.inputFile = input()

        img = ""

        img = Image.open(Data.FileLocations.inputFile)
        img = img.convert("RGB")

        #print(img)
        width, height = img.size
        px = img.load()

        if width > 32 or height > 32:
            print("file too big - need to be at most 32x32")
        else:
            fr._getPixels(width, height, px)

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