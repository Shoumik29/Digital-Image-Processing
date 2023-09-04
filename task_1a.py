import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = 'sample_image.jpg'


def downsample(image, scale):
	h, w = image.shape
	r_h, r_w = h//scale, w//scale
	
	resized_image = np.zeros((r_h, r_w))
	
	for i in range(r_h):
		for j in range(r_w):
			resized_image[i,j] = image[i*scale, j*scale]
	
	return resized_image


def main():

	image = cv2.imread(image_path) #loading image
	image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #converting to gray
	
	image_list = []
	
	image_list.append(image)
	
	resized_image = downsample(image,10)
	
	image_list.append(resized_image)

	for i in range(len(image_list)):
		plt.subplot(1,2,i+1)
		plt.imshow(image_list[i], cmap='gray')
	plt.show()


if __name__ == '__main__':
	main()

