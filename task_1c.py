import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = 'sample_image.jpg'


def main():
	
	image = cv2.imread(image_path) #loading image
	image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #converting to gray
	
	h,w = image.shape
	
	freq = np.zeros(256, dtype=np.uint8)
	
	
	for i in range(0,h):
		for j in range(0,w):
			freq[image[i,j]] += 1
		
	
	for i in range(0,h):
		for j in range(0,w):
			if image[i,j] >= 200:
				image[i,j] = 255
			else:
				image[i,j] = 0
				
				
		
				
	plt.imshow(image, cmap='gray')
	plt.show()	

	#ploting histogram
	plt.figure(figsize = (10, 5))
	plt.bar(range(256), np.array(freq))
		
	plt.xlabel("Pixel intensity")
	plt.ylabel("Frequency")
	plt.title("Histogram")
	plt.show()
		
	
		
		
	
	


if __name__ == '__main__':
	main()
