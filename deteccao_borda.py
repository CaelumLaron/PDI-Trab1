import sys
import cv2
import numpy as np


def color_quantization(img, K):
	Z = img.reshape((-1,3))
	Z = np.float32(Z)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
	return res2

def load_image( infilename ):
	img = cv2.imread(infilename)
	img = color_quantization(img, 32)
	return np.asarray(img, dtype="int32")

def save_image(data):
	return np.asarray(np.clip(data, 0, 255), dtype='uint8')

def robert_cross(infilename):
	img = load_image(infilename)
	gradient = lambda i,j: np.sqrt(np.square(img[i][j]-img[i+1][j+1]) + np.square(img[i][j+1]-img[i+1][j]))
	for i in range(len(img)-1):
		for j in range(len(img[0])-1):
			img[i][j] = gradient(i,j)
	out = save_image(img)
	cv2.imshow('Robert', out)
	key = cv2.waitKey(0) & 0xFF

infilename = sys.argv[1]
print(infilename)
robert_cross(infilename)