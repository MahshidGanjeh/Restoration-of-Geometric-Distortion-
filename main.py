import numpy as np
import cv2

from matplotlib import pyplot as plt

image = cv2.imread('sample.jpg')
# cv2.imshow('image',image)
# key = cv2.waitKey()
# if key == 27:
#   cv2.destroyAllWindows()

img = cv2.line(image, (0, 0), (314, 101), (0, 255, 0), 4)
cv2.imshow('img', img)
cv2.waitKey(0)
# value e pixel radif 100 va sotune 100 ra neshan midahad
px = image[100, 100]
#print(px)
# B=0G=1R=2
blue = image[100, 100, 0]
#print(blue)
image[100, 100] = [255, 255, 255]

#print(image.item(100, 100, 0))

# modifying RED value
image.itemset((10, 10, 2), 100)
print(image.item(10, 10, 2))

# Accessing Image Properties
# It returns a tuple of number of rows, columns and channels (if image is color):
print(image.shape)
print(image.size)
