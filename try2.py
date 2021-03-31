import cv2
import numpy as np 

img = cv2.imread("rod2.png")
img_re = cv2.resize(img,(10,10))
img_re = cv2.cvtColor(img_re,cv2.COLOR_BGR2GRAY)

img1 = cv2.addWeighted(img_re,0.23,img_re,0.0,0)
img2 = img_re * 0.23

print(img_re)
print(img1)
print(img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
#cv2.imshow("img3",img3)
cv2.waitKey(0)