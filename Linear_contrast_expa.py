import numpy as np
import cv2 

def _z(z):
	if z <= 85:
		return z//2
	elif 85<z<170:
		return 2*z - 127
	else:
		return (z//2) + 128

img = cv2.imread("Ursos.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow('Ursos.jpg', img)
key = cv2.waitKey(0) & 0xFF

for i in range(len(img)):
	for j in range(len(img[i])):
		img[i][j] = _z(img[i][j])

cv2.imshow('Ursos.jpg', img)
key = cv2.waitKey(0) & 0xFF