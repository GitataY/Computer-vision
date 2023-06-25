import cv2

# Load the classifiers
cat_face_classifier = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

# Load the cat image
image = cv2.imread('cat.jpg')

# Convert the image to grayscale for detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform cat face detection
cat_faces = cat_face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Loop through the detected cat faces
for (x, y, w, h) in cat_faces:
    # Extract the region of interest (cat face) from the grayscale image
    roi_gray = gray[y:y + h, x:x + w]
    
    # Perform eye detection within the cat face region
    eyes = eye_classifier.detectMultiScale(roi_gray)
    
    # Loop through the detected eyes and draw rectangles
    for (ex, ey, ew, eh) in eyes:
        # Calculate the coordinates of eyes relative to the original image
        eye_x = x + ex
        eye_y = y + ey
        
        # Draw rectangles around the detected eyes
        cv2.rectangle(image, (eye_x, eye_y), (eye_x + ew, eye_y + eh), (0, 255, 0), 2)

# Display the image with the drawn rectangles
cv2.imshow('Cat Eye Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
