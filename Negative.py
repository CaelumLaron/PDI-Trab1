import numpy as np 
import cv2

img = cv2.imread('lena_color.png')
for i in range(len(img)):
	for j in range(len(img[i])):
		for k in range(len(img[i][j])):
			img[i][j][k] = 255 - img[i][j][k] 
cv2.imshow('test', img)
key = cv2.waitKey(0) & 0xFF