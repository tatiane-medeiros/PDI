import numpy as np
import cv2

im = cv2.imread("baboon.png")
col = im[0].size
row = im.size/col
col = col/3
img = im[int(col/2):, int(row/4):-int(row/4)]

cv2.imwrite("newbaboon.png", img)
