#Read a video from web Cam using openCV
import cv2
import numpy as np

# create a Camera object

cam = cv2.VideoCapture(0)

#Ask the name
fileName = input("Enter the name of the person :")
dataset_path = "/Users/apple/Desktop/facedetect/data/"
offset=20

#model
model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#create a list of save face data

faceData = []
skip = 0

# read image from Camera object

while True:
    success,img = cam.read()
    if not success:
        print("Reading Camera Failed")
     
    #storage the gray images
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = model.detectMultiScale(img,1.1,5)
    
    #pick the face with largest bounding box
    faces = sorted(faces,key=lambda f:f[2]*f[3])
    
    #pick the largest face
    
    if len(faces)>0:
        f = faces[-1]
    
        x,y,w,h = f
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
        #crop and save the largest face
        cropped_face = img[y-offset:y+h+offset,x-offset:x+offset+w]
    
        cropped_face = cv2.resize(cropped_face,(100,100))
        skip += 1
        if skip % 10 == 0:
            faceData.append(cropped_face)
            print("Saved so far" + str(len(faceData)))
        
        faceData.append(cropped_face)
        
    cv2.imshow('Image window', img)
    #cv2.imshow('Cropped Face',cropped_face)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
        
# write the facedata on the disk

faceData = np.asarray(faceData)
m = faceData.shape[0]
faceData = faceData.reshape((m,-1))

#Save on the disk as np array
filePath = dataset_path + fileName + ".npy"
np.save(filePath,faceData)
print("data save successfullly:" + filePath)


        
# release Camera , and destroy window
cam.release()
cv2.destroyAllWindows()