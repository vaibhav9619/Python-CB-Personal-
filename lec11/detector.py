import numpy as np
import cv2
import time
# count=0
from PIL import Image

detector=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces=detector.detectMultiScale(gray)
    # print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        # mask=Image.open('c2.png')
        # mask=mask.resize((w,h),Image.ANTIALIAS)
        # offset=(x,y)
    cv2.imshow("image",img)


    # cv2.imwrite("images/"+ str(count)+ "image.jpg",img)
    # count+=1

    cv2.waitKey(1)