import cv2
import numpy as np

img=cv2.imread("12.jpg")
img1=cv2.imread("13.jpg")


# surf=cv2.xfeatures2d.SURF_create()
# sift=cv2.xfeatures2d.SIFT_create()
orb=cv2.ORB_create()

# kp=sift.detect(img, None)
keypoints, descriptors= orb.detectAndCompute(img, None)
keypoints1, descriptors1= orb.detectAndCompute(img1, None)

#brute force method
bf=cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches=bf.match(descriptors, descriptors1)
matches=sorted(matches, key= lambda x: x.distance)

for n in matches:
    print(n.distance)

matching_result= cv2.drawMatches(img, keypoints, img1, keypoints1, matches[:50],None, flags=2)

cv2.imshow("canny", img)
cv2.imshow("canny1", img1)
cv2.imshow("result", matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()