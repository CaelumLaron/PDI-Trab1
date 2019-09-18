import numpy as np
import cv2
import sys

def color_quantization(img, K):
	Z = img.reshape((-1,3))
	Z = np.float32(Z)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
	return res2


def bic(infilename):
	colors = {}
	img = cv2.imread(infilename)
	img = color_quantization(img, 64)
	color = lambda i, j: int(img[i][j][0]) + 4 * int(img[i][j][1]) + 16 * int(img[i][j][2]) #bgr
	limiar = lambda i, j: True if color(i,j) == color(i+1,j) == color(i+1, j+1) == color(i,j+1) else False
	histI, histB = np.zeros(64), np.zeros(64)
	for i in range(len(img) - 1):
		for j in range(len(img[0]) - 1):
			c = color(i,j)
			if not c in colors:
				colors[c] = len(colors)
			if limiar(i,j):
				histI[colors[c]] += 1
			else:
				histB[colors[c]] += 1
	cv2.imshow('Lena', img)
	key = cv2.waitKey(0) & 0xFF
	print(histB, histI)

infilename = sys.argv[1]
bic(infilename)