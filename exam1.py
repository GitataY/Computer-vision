import cv2 as cv

img = cv.imread('photos/profile.jpg')

cv.imshow('profile', img)

cv.waitKey(0)