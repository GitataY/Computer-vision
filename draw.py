import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('blank', blank)

# pant the image a color

blank[:] = 0,255,0
cv.imshow('Green', blank)

# draw a rectangle
cv.rectangle(blank, (0,0), (200,200), (0,0,0), thickness=-1)
cv.imshow('rectangle', blank)

# draw a line 
cv.line(blank, (10,10), (300,300), (0,0,255), thickness=1)
cv.imshow('line', blank)



# Write text
cv.putText(blank, 'Hello Yvonne',(255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), 2)
cv.imshow('putText', blank)

cv.waitKey(0)

