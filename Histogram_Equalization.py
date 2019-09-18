import numpy as np
import cv2

DEBUG = False

img = cv2.imread('photo_2019-09-16_15-59-29.jpg', cv2.IMREAD_GRAYSCALE)

#cv2.imshow('Ursos.jpg', img)
key = cv2.waitKey(0) & 0xFF

hist = np.zeros(256, np.intc)

N = len(img) * len(img[0])
L = 256

for i in range(len(img)):
	for j in range(len(img[i])):
		hist[img[i][j]] += 1

nhist = np.zeros(L, np.double)

for i in range(L):
	nhist[i] = hist[i]/N

if DEBUG:
	print(nhist)
fhist = np.zeros(L, np.double)
fhist[0] = nhist[0]

for i in range(1,L):
	fhist[i] = fhist[i-1] + nhist[i]

if DEBUG:
	print(fhist)
ifthist = np.zeros(L, np.intc)

for i in range(L):
	ifthist[i] = fhist[i]*(L-1) + .5

if DEBUG:
	print(ifthist)
_hist = np.zeros(L, np.intc)

for i in  range(L):
	_hist[ifthist[i]] += hist[i]

if DEBUG:
	print(_hist)

for i in range(len(img)):
	for j in range(len(img[i])):
		img[i][j] = ifthist[img[i][j]]

cv2.imshow('Ursos.jpg', img)
key = cv2.waitKey(0) & 0xFF