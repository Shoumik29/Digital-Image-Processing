import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'sample_image.jpg'

def decimal_to_binary(num):
	n = []
	while(num):
		n.append(num%2)
		num = num//2
	return n

def binary_to_decimal(n):
	dec = 0
	for i in range(len(n)):
		dec = dec + (n[i]*(2**i))
	return dec
	
def dec_ilr(image, num_bit):
	h, w = image.shape
	dec_image = np.zeros((h, w))
	for i in range(h):
		for j in range(w):
			if image[i,j]==0:
				continue
			binary_list = decimal_to_binary(image[i,j])
			for p in range(num_bit):
				if len(binary_list)>0:
					binary_list.pop()
			dec_image[i,j] = binary_to_decimal(binary_list)
	return dec_image

def main():

	image = cv2.imread(image_path) #loading image
	image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #converting to gray
	
	image_list = []
	
	image_list.append(image)
	
	dec_image = dec_ilr(image, 3)
	
	image_list.append(dec_image)
	
	for i in range(len(image_list)):
		plt.subplot(1,2,i+1)
		plt.imshow(image_list[i], cmap='gray')
	plt.show()



if __name__ == '__main__':
	main()
