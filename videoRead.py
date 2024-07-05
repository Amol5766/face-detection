#Read a video from web Cam using openCV
import cv2

# create a Camera object

cam = cv2.VideoCapture(0)

# read image from Camera object

while True:
    success,img = cam.read()
    if not success:
        print("Reading Camera Failed")
        
    cv2.imshow('Image window', img)
    cv2.waitKey(1)