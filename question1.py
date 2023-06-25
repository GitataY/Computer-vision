import cv2

car_classifier = cv2.CascadeClassifier('cars.xml')

video = cv2.VideoCapture('cars.mp4')

while video.isOpened():
    ret, frame = video.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cars = car_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow('Car Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

video.release()
cv2.destroyAllWindows()
