import cv2
import numpy as np
from collections import Counter 
import time
import collections


def nothing(x):
    pass

cv2.namedWindow('image')
cv2.namedWindow('can')
cv2.namedWindow('blur')
cv2.namedWindow('Trackbars')

cv2.createTrackbar('A','image',0,100,nothing)
cv2.createTrackbar('B','image',0,100,nothing)
cv2.createTrackbar('C','image',0,100,nothing)
cv2.createTrackbar('D','image',0,100,nothing)
cv2.createTrackbar('E','image',0,100,nothing)
cv2.createTrackbar('F','image',0,100,nothing)
cv2.createTrackbar('G','image',0,100,nothing)
cv2.createTrackbar('H','image',0,100,nothing)

cv2.createTrackbar('I','can',0,300,nothing)
cv2.createTrackbar('J','can',0,300,nothing)

cv2.createTrackbar('K','blur',0,25,nothing)
cv2.createTrackbar('L','blur',0,25,nothing)
cv2.createTrackbar('M','blur',0,25,nothing)
cv2.createTrackbar('N','blur',0,25,nothing)
cv2.createTrackbar('O','blur',0,25,nothing)

cv2.createTrackbar('L1','Trackbars',1,255,nothing)
cv2.createTrackbar('L0','Trackbars',1,255,nothing)
cv2.createTrackbar('L2','Trackbars',1,255,nothing)




# load the image, convert it to grayscale, blur it slightly,
# and threshold it

while(1) :

    a  = cv2.getTrackbarPos('A','image')
    b1  = cv2.getTrackbarPos('B','image')
    c  = cv2.getTrackbarPos('C','image')
    d  = cv2.getTrackbarPos('D','image')
    e  = cv2.getTrackbarPos('E','image')
    f  = cv2.getTrackbarPos('F','image')
    g1 = cv2.getTrackbarPos('G','image')
    h  = cv2.getTrackbarPos('H','image')

    i  = cv2.getTrackbarPos('I','can')
    j  = cv2.getTrackbarPos('J','can')

    k  = cv2.getTrackbarPos('K','blur')
    l  = cv2.getTrackbarPos('L','blur')
    m  = cv2.getTrackbarPos('M','blur')
    n  = cv2.getTrackbarPos('N','blur')
    o  = cv2.getTrackbarPos('O','blur')

    L1 = cv2.getTrackbarPos('L1','Trackbars')
    L0 = cv2.getTrackbarPos('L0','Trackbars')
    L2 = cv2.getTrackbarPos('L2','Trackbars')

    img_ = cv2.imread('splitm1.jpg')
    img_re = cv2.resize(img_,(600,600))


    color_planes = cv2.split(img_re)
    planes=color_planes
    planes[0]=(color_planes[0])*(L0)
    planes[1]=(color_planes[1])*(L1)
    planes[2]=(color_planes[2])*(L2)
#   print("r",planes[0])

    img = cv2.merge(planes)

    b,g,r=cv2.split(img)
    B,G,R=list(map(cv2.equalizeHist,[b,g,r]))

    Bgr=cv2.merge((B,g,r))
    BgR=cv2.merge((B,g,R))   
    BGR=cv2.merge((B,G,R))
    BGr=cv2.merge((B,G,r))
    bGR=cv2.merge((b,G,R))
    bgr=cv2.merge((b,g,r))
    bGr=cv2.merge((b,G,r))
    bgR=cv2.merge((b,g,R))


    T1 = cv2.addWeighted(Bgr,a/100.0,BGr,b1/100.0,0)
    T2 = cv2.addWeighted(BGR,c/100.0,BgR,d/100.0,0)
    T3 = cv2.addWeighted(bgr,e/100.0,bGR,f/100.0,0)
    T4 = cv2.addWeighted(bGr,g1/100.0,bgR,h/100.0,0)
    T5 = cv2.addWeighted(T1,1,T2,1,0)
    T6 = cv2.addWeighted(T3,1,T4,1,0)
    T7 = cv2.addWeighted(T5,1,T6,1,0)

    #blurT = cv2.GaussianBlur(T7,(5,5),0)   
    blurT = cv2.fastNlMeansDenoisingColored(T7,None,k,l,m,n)
    grayT = cv2.cvtColor(blurT,cv2.COLOR_BGR2GRAY)

    edgesT = cv2.Canny(grayT,i,j,apertureSize = 3)
    img1 = cv2.dilate(edgesT,(5,5),iterations =2*o +1)
    img2 = cv2.bitwise_not(img1)
    cv2.imshow('img1',img1)
    cv2.imshow('img',img)
    
    cv2.imshow('img2',img2)
    cv2.imshow('T7',T7)
    cv2.imwrite("splitm2.jpg",img2)
    if cv2.waitKey(1) == 27:
        cv2.imwrite("splitm2.jpg",img2)
        break

