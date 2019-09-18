import cv2
import numpy as np
import sys
from scipy import stats

M = 20

k = int(sys.argv[2])

def limiar(value, compare):
	if abs(value - compare) > M:
		return compare
	else:
		return value

def getMean(n, m, l, img):
	numbers = np.zeros(k*k)
	for i in range(k):
		for j in range(k):
			numbers[3*i+j] = img[n+i][m+j][l] 
	answer = limiar(img[n][m][l], sum(numbers)/(k*k))
	return answer

def getMedian(n, m, l, img):
	numbers = np.zeros(k*k)
	for i in range(k):
		for j in range(k):
			numbers[3*i+j] = img[n+i][m+j][l] 
	numbers.sort()
	median = 0
	m = (k*k)//2
	if k%2 == 0:
		median = numbers[m]
	else:
		median = (numbers[m] + numbers[m+1])/2
	answer = limiar(img[n][m][l], median)
	return answer

def getMode(n,m,l,img):	
	numbers = np.zeros(k*k)
	for i in range(k):
		for j in range(k):
			numbers[3*i+j] = img[n+i][m+j][l] 
	mode = stats.mode(numbers)[0]
	answer = limiar(img[n][m][l], mode)
	return answer

def modeFilter(infilename):
	img = cv2.imread(infilename)
	for i in range(len(img) - k - 1):
		for j in range(len(img) - k - 1):
			for l in range(3):
				img[i][j][l] = getMode(i, j, l, img)
	cv2.imshow('Lena', img)
	p = cv2.waitKey(0) & 0xFF

def meanFilter(infilename):
	img = cv2.imread(infilename)
	for i in range(len(img) - k - 1):
		for j in range(len(img) - k - 1):
			for l in range(3):
				img[i][j][l] = getMean(i, j, l, img)
	cv2.imshow('Lena', img)
	p = cv2.waitKey(0) & 0xFF

def medianFilter(infilename):
	img = cv2.imread(infilename)
	for i in range(len(img) - k - 1):
		for j in range(len(img) - k - 1):
			for l in range(3):
				img[i][j][l] = getMedian(i, j, l, img)
	cv2.imshow('Lena', img)
	p = cv2.waitKey(0) & 0xFF


infilename = sys.argv[1]
modeFilter(infilename)