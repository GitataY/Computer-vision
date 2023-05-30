import cv2 as cv

img = cv.imread('photos/pineapple.jpg')

cv.imshow('pineapple', img)

def rescaleframe(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleframe(img)
cv.imshow('image', resized_image)



cv.waitKey(0)