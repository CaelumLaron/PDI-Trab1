import numpy as np
import cv2

DEBUG = False # Show the local areas

img = cv2.imread('lena_color.png') # Image

a = int(input("Entrada: ")) # Number of divisions in a format axa
n, m = len(img)//a, len(img[0])//a # Size of image

g = [[0 for i in range(256)] for j in range(a * a)]
r = [[0 for i in range(256)] for j in range(a * a)]
b = [[0 for i in range(256)] for j in range(a * a)]

for i in range(len(img)):
	for j in range(len(img[i])):
		for k in range(len(img[i][j])):
			pos =  a * ((i//n) - ((i//n) >= a)) + ((j // m) - ((j//m) >= a))
			if DEBUG and pos % 2 == 0:
				img[i][j] = ~img[i][j]
			if k == 0:
				g[pos][img[i][j][k]] += 1
			elif k == 1:
				r[pos][img[i][j][k]] += 1
			else:
				b[pos][img[i][j][k]] += 1

cv2.imshow('test', img) #Show image
key = cv2.waitKey(0) & 0xFF

hg, hr, hb = g[0], r[0], b[0]

for i in range(1, len(g)):
	hg = hg + g[i]

for i in range(1, len(r)):
	hr = hr + r[i]

for i in range(1, len(b)):
	hb = hb + b[i]

print(len(hg), len(hr), len(hb))

ag = open("lena_color_g_hist_local.txt", "w+")
ag.write(str(hg))
ag.close()

ar = open("lena_color_r_hist_local.txt", "w+")
ar.write(str(hr))
ar.close()

ab = open("lena_color_b_hist_local.txt", "w+")
ab.write(str(hb))
ab.close()

print('Terminei!')