import cv2 as cv
cap = cv.VideoCapture('Cars.mp4')
while True:
	ret, im = cap.read()
	cv.imshow('playvideotest',im)
	if cv.waitKey(20) & 0xFF == ord('q'):
		break
cap.release()
cv.destroyAllWindows()