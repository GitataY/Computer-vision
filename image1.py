import cv2 as cv

img = cv.imread('photos/banana2.jpg')

cv.imshow('banana', img)

cv.waitKey(0)