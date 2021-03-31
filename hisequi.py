import cv2
import numpy as np 

im = cv2.imread('rod.jpg')
img = cv2.resize(im,(500,500))
original_img = img


B = original_img[:,:,0]
G = original_img[:,:,1]
R = original_img[:,:,2]

B_equ = cv2.equalizeHist(B)
G_equ = cv2.equalizeHist(G)
R_equ = cv2.equalizeHist(R)


original_img[:,:,0] = B_equ
original_img[:,:,1] = G_equ
original_img[:,:,2] = R

cv2.imshow("image",original_img)

cv2.waitKey(0)

