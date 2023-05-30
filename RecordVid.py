import cv2 as cv
cap = cv.VideoCapture(0)
while True:
	ret,img = cap.read()
	cv.imshow ('video', img)
	
	key = cv.waitKey(1) 
	if key == 27:
		break
cap.release()
cv.destroyAllWindows()