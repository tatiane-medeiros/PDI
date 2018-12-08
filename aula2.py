# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:26:15 2018

@author: tatiane
"""

import numpy as np
import cv2
print(cv2.__version__)

path = "deco.png"
path2 = "paper.png"

img = cv2.imread(path) #,cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(path2)
print(img.shape)
print(img2.shape)
#deixa do mesmo tamanho
new = cv2.resize(img,(int(400),int(400)))
n = cv2.resize(img2,(int(400),int(400)))
print(new.shape)
#cv2.namedWindow("main", cv2.WINDOW_NORMAL)
#sobrepõe imagens
dst = cv2.addWeighted(new,0.9,n,0.7,0)
cv2.imshow('colored', dst)
#reflete
ref = cv2.flip(dst,1)
cv2.imshow('reflected', ref)
#rotaciona
rows,cols,e3 = dst.shape
x = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(dst,x,(cols,rows))
cv2.imshow('rotation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
