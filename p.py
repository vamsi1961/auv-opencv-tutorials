import cv2
import numpy as np  

img = cv2.imread("test.jpg")
img = cv2.resize(img,(600,600))

gaussian = cv2.GaussianBlur(img,(5,5),0)


# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# clahe_output = clahe.apply(gaussian)


lab = cv2.cvtColor(gaussian, cv2.COLOR_BGR2LAB)

lab_planes = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))

lab_planes[0] = clahe.apply(lab_planes[0])

lab = cv2.merge(lab_planes)

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

img1 = cv2.cvtColor(bgr,cv2.COLOR_BGR2YCrCb)


B = img1[:,:,0]
G = img1[:,:,1]
R = img1[:,:,2]

Y_equ = cv2.equalizeHist(B)

img1[:,:,0] = Y_equ

median = cv2.medianBlur(img1,5)

image = cv2.cvtColor(median,cv2.COLOR_YCrCb2BGR)

cv2.imshow("img",median)

cv2.waitKey(0)

