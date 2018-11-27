import numpy as np
import cv2

#colors
palette = np.array([[0,0,0], [128,128,128]])
#black
image1 = np.array( [ [ 0  for n in range(400)] for n in range(400) ] )
img = palette[image1]
cv2.imwrite("black.png", img)
#gray
image2 = np.array( [ [ 1  for n in range(400)] for n in range(400) ] )
img = palette[image2]
cv2.imwrite("gray.png", img)
