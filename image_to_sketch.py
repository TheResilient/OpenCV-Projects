# This program converts an image to a sketch using a CV

import cv2

#get the image
img_location = 'images/input.jpg'
#read the image
img = cv2.imread(img_location)

#show the image
cv2.imshow('Original Image', img)
cv2.waitKey(0)

