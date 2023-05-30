import numpy as np
import matplotlib.pyplot as plt

# Read the image using Matplot
img = plt.imread('imagee.jpg')

# Print the array
#print(img)

x=np.array(img)
#print(x)

plt.imshow(x, cmap='gray')
plt.show()
