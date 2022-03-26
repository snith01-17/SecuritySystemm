#Importing libraries
from distutils.command.upload import upload
from os import access
import cv2
from numpy import number
import dropbox
import time
import random

startTime = time.time()

def takeSnapshot():
    number = random.randint(0,100)

    #To turn on the camera
    videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True

    while(result):
        #Reading the frames when camera is on
        ret, frame = videoCaptureObject.read()

        #storing the image
        imageName = "img"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        startTime = time.time
        result = False 
    return imageName
    print("Snapshot taken")    

    #Turning of the camera
    videoCaptureObject.release()

    #Destroying all the windows which could be opened by the camera
    cv2.destroyAllWindows()

def uploadFile(imageName):
    accessToken = "sl.BEGWWZhwIAM4xkkz-pBhC9SeFP8UMMFpjCMuIGXmljKrGMZre24PWVerPth6v0AmymdawXrraWe1VWvbl0XLkiZXVjW9eP5UpKGhEXhN4HYPAprbk80G2JzFtrNeJ5Ph8AZ6a9aC7Hk"
    file = imageName
    file_from = file
    file_to = "/newFolder"+(imageName)
    dbx = dropbox.Dropbox(accessToken)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File has been uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=600):
            name = takeSnapshot()
            uploadFile(name)


main()            