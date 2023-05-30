import cv2 as cv
import numpy as np

img = cv.imread("Nadia_Murad.jpg")
face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_alt.xml')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 3)

no_faces = len(faces)
print(no_faces)
print(faces)


for x,y,w,h in faces:
    
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    #cv.imshow('img', img)
    
    k = cv.waitKey(0) & 0xff
    if k==27:
        break

       
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()