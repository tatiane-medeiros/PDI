import numpy as np
import cv2


img = cv2.imread("lena.png")
col = img[0].size
row = int(img.size/col)
col = int(col/3)
im = img.copy()
#darker image
for i in range(row):
   for j in range(col):         
        im[i][j][0] = img[i][j][0] - 80 if img[i][j][0] > 80 else 0
        im[i][j][1] = img[i][j][1] - 80 if img[i][j][1] > 80 else 0
        im[i][j][2] = img[i][j][2] - 80 if img[i][j][2] > 80 else 0
        
cv2.imwrite("darker.png", im)
#lighter  image    
for i in range(row):
   for j in range(col):         
        img[i][j][0] = img[i][j][0] + 80 if img[i][j][0] < 175 else 255
        img[i][j][1] = img[i][j][1] + 80 if img[i][j][1] < 175 else 255
        img[i][j][2] = img[i][j][2] + 80 if img[i][j][2] < 175 else 255
   
cv2.imwrite("lighter.png", img)
