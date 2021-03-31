import cv2
import numpy as np

im = cv2.imread('test.jpg', 0)
img = cv2.resize(im,(800,800))  


def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('A_ero','image',0,2,nothing)        #erosion element max=2
cv2.createTrackbar('B_ero','image',1,21,nothing)      #kernel size for erosion max=21
cv2.createTrackbar('C_dil','image',0,2,nothing)          #dilation element max=2
cv2.createTrackbar('D_dil','image',1,21,nothing)         #kernel size for dilation max=21
cv2.createTrackbar('E_ero','image',0,5,nothing)         # itrations for erosion 
cv2.createTrackbar('F_dil','image',0,5,nothing)         # iterations for dilation 

while (1):
    
    a  = cv2.getTrackbarPos('A_ero','image')
    b  = cv2.getTrackbarPos('B_ero','image')
    c  = cv2.getTrackbarPos('C_dil','image')
    d  = cv2.getTrackbarPos('D_dil','image')
    e  = cv2.getTrackbarPos('E_ero','image')
    f  = cv2.getTrackbarPos('F_dil','image')


    if (a==0):
        kernal_e=cv2.getStructuringElement(cv2.MORPH_RECT,(2*b+1,2*b+1))
    if (a==1):
       kernal_e=cv2.getStructuringElement(cv2.MORPH_CROSS,(2*b+1,2*b+1))
    if (a==2):
        kernal_e=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*b+1,2*b+1))

    # kernal_e=cv2.getStructuringElement(cv2.erosion_type,(2*b+1,2*b+1))

   
    if (c==0):
        kernal_d=cv2.getStructuringElement(cv2.MORPH_RECT,(2*d+1,2*d+1))
    if (c==1):
        kernal_d=cv2.getStructuringElement(cv2.MORPH_CROSS,(2*d+1,2*d+1))
    if (c==2):
        kernal_d=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*d+1,2*d+1))

    # kernal_d=cv2.getStructuringElement(cv2.dilation_type,(2*d+1,2*d+1))

    img_ero = cv2.erode(img, kernel_e, iterations= e)
    img_dilation = cv2.dilate(img_ero, kernel_d, iterations= f)

    # cv2.imshow('Input', img)
    # cv2.imshow('Erosion', img_erosion)
    cv2.imshow('Dilation', img_dilation)

    if cv2.waitKey(1) == 27:
        break