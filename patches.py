import cv2
import numpy as np
import matplotlib.pyplot as plt

image_size = 32
image_path = 'sample_image.jpg'

img = cv2.imread(image_path)

# convert RGB to BGR
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

height, width, channels = img.shape
print(height, width, channels)

W_SIZE = 3  
H_SIZE = 3

patch_list = []

#resized_img = cv2.resize(img, (image_size, image_size))

#height, width, channels = resized_img.shape
#print(height, width, channels)

binary_img = np.zeros((height, width, channels))



print(binary_img.shape)

for i in range(height):
	for j in range(width):
		if(gray_img[i][j]!=255):
			binary_img[i][j] = 255

plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(binary_img)
plt.show()

'''for ih in range(H_SIZE ):
   for iw in range(W_SIZE ):
   
      x = width/W_SIZE * iw 
      y = height/H_SIZE * ih
      h = (height / H_SIZE)
      w = (width / W_SIZE )
     
      patch_list.append(img[int(y):int(y+h), int(x):int(x+w)]) 
      
      img[int(y):int(y+h), int(x):int(x+w)]

for i in range(0,9):
	plt.subplot(3,3,i+1)
	plt.imshow(patch_list[i])
plt.show()'''
