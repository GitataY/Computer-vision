import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image using OpenCV
img = cv2.imread('imagee.jpg')
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert the image to a NumPy array
img_arr = np.array(RGB_img)

# Display array
plt.imshow(img_arr)
plt.show()
