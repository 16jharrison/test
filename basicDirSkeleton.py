import os 
import sys
from pathlib import Path

#this program takes in arugments in the teminal to create a dir 
#skeleton, a basic read me file is added to the Dirs so we can
#upload them using git.(which only tracks non empty directories )


#note that the first augrment is true or false based on needing
#an index.Html File
def createFiles(dirArray):
    mainPath = os.getcwd()

    for dirName in dirArray[1:] : 
        os.mkdir(dirName)
        os.chdir(mainPath + '/' + dirName )
        Path(mainPath + '/' + dirName + "/read.txt").touch()
        os.chdir(mainPath)

    if dirArray[0] == "true" : Path(mainPath + '/' + "/index.html").touch()

inputArr = sys.argv[1:]
createFiles(inputArr)