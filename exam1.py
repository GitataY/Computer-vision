import cv2 as cv

img = cv.imread('photos/profile.jpg')

cv.imshow('profile', img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray person', gray)

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

print(f'Number of faces = {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), color= (0,255,0), thickness=2)

cv.imshow('detected faces', img)



cv.waitKey(0)