import numpy as np
import cv2
# img=np.zeros((500,500,3),np.uint8)
face=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
img=cv2.VideoCapture(0)
while True:
    ret,cap=img.read()
    # cv2.line(cap,(100,100),(200,200),(0,0,255),2)
    cv2.rectangle(cap,(100,100),(200,200),(0,0,0),30)
    cv2.line(cap,(220,150),(300,150),(0,0,0),2)
    cv2.line(cap,(220,155),(300,155),(0,0,0),2)
    cv2.rectangle(cap,(300,100),(400,200),(0,0,0),30)
    # cv2.line(cap,(300,100),(400,200),(0,0,255),2)
    # cv2.circle(cap,(150,150), 30, (0,0,0), -1)
    # cv2.circle(cap,(350,150), 30, (0,0,0), -1)
    cv2.line(cap, (260,300), (350, 350), (0, 0, 0), 30)

    cv2.imshow("jsd",cap)
    cv2.waitKey(1)
    # cv2.destroyAllWindows()