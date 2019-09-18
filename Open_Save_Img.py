import numpy as np 
import cv2

img = cv2.imread('img_1.jpeg')
#img = cv2.imread('img_1.jpeg', cv2.IMREAD_COLOR) #Loads a color image (Default).
#img = cv2.imread('img_1.jpeg', cv2.IMREAD_GRAYSCALE) #Loads image in a gray scale mode
#img = cv2.imread('img_1.jpeg', cv2.IMREAD_UNCHANGED) #Loads image as such including alpha channel
cv2.imshow('Test', img)
key = cv2.waitKey(0) & 0xFF
if key == 27:
	cv2.destroyAllWindows()
elif key == ord('s'):
	cv2.imwrite('img_1_invert.png', img)
	cv2.destroyAllWindows()