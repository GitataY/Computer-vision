import cv2 as cv
import numpy as np

img = cv.imread("cat3.jpg")
face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalcatface.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_eye.xml')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

no_faces = len(faces)
print(no_faces)
print(faces)


for x,y,w,h in faces:
    
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
    
    for ex,ey,ew,eh in eyes:
    		cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
    		cv.imshow('eye-show', roi_color)  
    
    #cv.imshow('img', img)
    
    k = cv.waitKey(0) & 0xff
    if k==27:
        break

       
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()
