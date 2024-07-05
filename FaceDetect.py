#Read a video from web Cam using openCV
import cv2

# create a Camera object

cam = cv2.VideoCapture(0)

#model
model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# read image from Camera object

while True:
    success,img = cam.read()
    if not success:
        print("Reading Camera Failed")
        
    faces = model.detectMultiScale(img,1.1,5)
    
    for f in faces:
        x,y,w,h = f
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
    cv2.imshow('Image window', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
        
# release Camera , and destroy window
cam.release()
cv2.destroyAllWindows()