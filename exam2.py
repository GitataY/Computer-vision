import cv2 as cv

capture = cv.VideoCapture('videos/girls.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('girls', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindowsc