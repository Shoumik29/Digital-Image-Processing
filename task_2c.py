import cv2
import math
import numpy as np
import matplotlib.pyplot as plt


image_path = 'sample_image.jpg'


def main():
	
	image = cv2.imread(image_path) #loading image
	image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #converting to gray
	
	h,w = image.shape
	
	for i in range(0,h):
		for j in range(0,w):
			image[i,j] = image[i,j] & 224
	
	

	plt.imshow(image, cmap='gray')
	plt.show()
	

if __name__ == '__main__':
	main()
