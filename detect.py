import cv2 as cv

img = cv.imread('photos/profile.jpg')
cv.imshow('profile', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('profile', gray)

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scalefactor=-1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

cv.waitKey(0)