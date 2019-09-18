import numpy as np
import cv2 

N = 255//4

def _z(z):
	n = z//N
	p = ((n + 1) * 255)//4
	a = z - (n * 255)//4
	return a * (255 // p)
	

img = cv2.imread("Ursos.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow('Ursos.jpg', img)
key = cv2.waitKey(0) & 0xFF

for i in range(len(img)):
	for j in range(len(img[i])):
		img[i][j] = _z(img[i][j])

cv2.imshow('Ursos.jpg', img)
key = cv2.waitKey(0) & 0xFF