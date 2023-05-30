import cv2
# Capture 
cap = cv2.VideoCapture('Cars.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')
while True:
	ret, frames = cap.read()
	gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)	
	cars = car_cascade.detectMultiScale(gray, 1.1, 4)	
	for (x,y,w,h) in cars:
		cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
		cv2.imshow('carsvideo', frames)	

	if cv2.waitKey(20) == 27:
		break
cap.release()
cv2.destroyAllWindows()
