import numpy as np 
import cv2

value = int(input())
img = cv2.imread('lena_color.png')

for i in range(len(img)):
	for j in range(len(img[i])):
		for k in range(len(img[i][j])):
			img[i][j][k] = min(img[i][j][k]+value, 255) 

cv2.imshow('Test', img)
key = cv2.waitKey(0) & 0xFF
