import numpy as np 
import cv2

v = [[0 for j in range(256)] for i in range(3)]

img = cv2.imread('lena_color.png')
for i in range(len(img)):
	for j in range(len(img[i])):
		for k in range(len(img[i][j])):
			v[k][img[i][j][k]] += 1

print(v)
