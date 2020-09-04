'''
import cv2
import numpy as np

def nothing(x): print(x)

cv2.namedWindow('Track')
cv2.createTrackbar('LD', 'Track',0, 255, nothing)
cv2.createTrackbar('LU', 'Track',0, 255, nothing)
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    l_d=cv2.getTrackbarPos('LD', 'Track')
    u_h=cv2.getTrackbarPos('LU', 'Track')        
    img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(img, l_d, u_h)
    cv2.imshow('',canny)
    key=cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
'''
import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    img=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _ , th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) #
    th2= cv.adaptiveThreshold(img,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 10)  #more clear image is obtainted
    # th2= cv.adaptiveThreshold(img ,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 10)  

    cv.imshow('image',frame)
    cv.imshow('th1',th1)
    cv.imshow('th2',th2)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv.destroyAllWindows()