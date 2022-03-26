from dbm.ndbm import library
from unittest import result

#cv2 is a library
import cv2
from cv2 import VideoCapture

def takeSnapshot():

    #To turn on the camera
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        #Reading the frames when camera is on
        ret, frame = videoCaptureObject.read()

        #storing the image
        cv2.imwrite("Image.jpg", frame)
        result = False

    #Turning of the camera
    videoCaptureObject.release()

    #Destroying all the windows which could be opened by the camera
    cv2.destroyAllWindows()


takeSnapshot()