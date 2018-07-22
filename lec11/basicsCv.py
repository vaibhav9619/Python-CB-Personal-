import numpy as np
import cv2
# img=np.zeros((400,400,3),np.uint8) #store 8 byte integers(each pixel RGB) R G B A (2 byte of R)(2 byte of G) (2 byte of B))(2 byte of A)
# RGB A (A is transparancy)
# (height,width,depth)
img=cv2.imread("ges12.jpg")

cv2.line(img,(100,100),(200,200),(0,0,255),2)
cv2.rectangle(img,(100,100),(200,200),(0,0,0),2)
cv2.line(img,(100,200),(200,100),(0,0,255),2)
cv2.imshow("my_image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()