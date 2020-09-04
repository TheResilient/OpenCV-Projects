import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
cap=cv2.VideoCapture(0)
# img=cv2.imread('messi5.jpg')
while cap.isOpened():
    _,img=cap.read()

    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 3)
        region_of_interest=gray[y:y+h, x:x+w]
        region_of_interest_color=img[y:y+h, x:x+w]
        smile=smile_cascade.detectMultiScale(region_of_interest)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(region_of_interest_color, (sx,sy), (sx+sw,sy+sh), (0,255,0),5)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
