import cv2
import numpy as np 

# def nothing(x):
#     pass

# cv2.namedWindow('image')


# original_img = img



# cv2.createTrackbar('Hlo','image',0,255,nothing)
# cv2.createTrackbar('Hup','image',0,255,nothing)
# cv2.createTrackbar('Slo','image',0,255,nothing)
# cv2.createTrackbar('Sup','image',0,255,nothing)
# cv2.createTrackbar('Vlo','image',0,255,nothing)
# cv2.createTrackbar('Vup','image',0,255,nothing)



# # load the image, convert it to grayscale, blur it slightly,
# # and threshold it

# while(1) :


#     Hlo = cv2.getTrackbarPos('Hlo','image')
#     Hup = cv2.getTrackbarPos('Hup','image')
#     Slo = cv2.getTrackbarPos('Slo','image')
#     Sup = cv2.getTrackbarPos('Sup','image') 
#     Vlo = cv2.getTrackbarPos('Vlo','image')
#     Vup = cv2.getTrackbarPos('Vup','image')
im = cv2.imread('sauvc.png')
img = cv2.resize(im,(500,500))
original_img = img
cv2.imshow('original',img)
B = original_img[:,:,0] 
G = original_img[:,:,1] 
R = original_img[:,:,2] 
    
B_equ = cv2.equalizeHist(B)
G_equ = cv2.equalizeHist(G)
R_equ = cv2.equalizeHist(R)

original_img[:,:,0] = B_equ
original_img[:,:,1] = G_equ
original_img[:,:,2] = R_equ 

cv2.imshow('show',original_img)


cv2.waitKey(0)