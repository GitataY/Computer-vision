import cv2 as cv
cap = cv.VideoCapture(0)
while True:
	ret,img = cap.read()
	cv.imshow ('myphoto', img)
	key = cv.waitKey(5000) 
	if cv.waitKey(5000) & 0xFF == ord('q'):
		cv.imwrite('Myself_Potrait.jpg',img)
	break
cap.release()
cv.destroyAllWindows()