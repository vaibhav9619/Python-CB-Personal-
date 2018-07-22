import numpy as np
import cv2
import time
detector=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces=detector.detectMultiScale(gray,2,5)
    # print(faces)
    if len(faces)>0:
        (x,y,w,h)=faces[0]
        face=img[y:y+h,x:x+w] #image chopping
        cv2.imshow("image", face)


    cv2.waitKey(1)