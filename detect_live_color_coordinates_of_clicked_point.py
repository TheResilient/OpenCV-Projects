import cv2 as cv
import numpy as np

# e=[i for i in dir(cv) if 'EVENT' in i]
# print(e)


def mouse_click(event, x, y, flags, params):
    if event==cv.EVENT_LBUTTONDOWN:
        circles1.append((x,y))
    
        

cap=cv.VideoCapture(0)
cv.namedWindow('hola')
cv.setMouseCallback('hola', mouse_click)

circles1=[]

while True:
    _, frame= cap.read()
    for center_circles in circles1:
        cv.circle(frame,center_circles, 5, (0,0,255), -1)
        center_circles=list(center_circles)
        font=cv.FONT_HERSHEY_SIMPLEX
        strXY= str(center_circles[0])+', '+str(center_circles[1])
        cv.putText(frame, strXY, (center_circles[0],center_circles[1]), font, 0.5, (255,0,0), 2)

        blue=frame[center_circles[0],center_circles[1],0]
        green=frame[center_circles[0],center_circles[1],1]
        red=frame[center_circles[0],center_circles[1],2]
        
        second = np.zeros((512,512,3), np.uint8)
        second[:]=[blue,green,red]

        cv.imshow('second window', second)


    
    
    cv.imshow('hola',frame)

    key=cv.waitKey(1)
    if key==27: break

cap.release()
cv.destroyAllWindows()