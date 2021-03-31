import cv2
import numpy as np
from collections import Counter 
import time
import collections


def nothing(x):
    pass

cv2.namedWindow('image')
cv2.namedWindow('ED')

cv2.createTrackbar('A','image',0,100,nothing)
cv2.createTrackbar('B','image',0,100,nothing)
cv2.createTrackbar('C','image',0,100,nothing)
cv2.createTrackbar('D','image',0,100,nothing)
cv2.createTrackbar('E','image',0,100,nothing)
cv2.createTrackbar('F','image',0,100,nothing)
cv2.createTrackbar('G','image',0,100,nothing)
cv2.createTrackbar('H','image',0,100,nothing)
cv2.createTrackbar('I','image',0,100,nothing)
cv2.createTrackbar('J','image',0,100,nothing)
cv2.createTrackbar('K','image',0,25,nothing)
cv2.createTrackbar('L','image',0,25,nothing)
cv2.createTrackbar('M','image',0,25,nothing)
cv2.createTrackbar('N','image',0,25,nothing)
cv2.createTrackbar('O','image',0,25,nothing)

cv2.createTrackbar('C2','ED',0,10,nothing)
cv2.createTrackbar('D2','ED',0,10,nothing)


# load the image, convert it to grayscale, blur it slightly,
# and threshold it

while(1) :

    a  = cv2.getTrackbarPos('A','image')
    b1  = cv2.getTrackbarPos('B','image')
    c  = cv2.getTrackbarPos('C','image')
    d  = cv2.getTrackbarPos('D','image')
    e  = cv2.getTrackbarPos('E','image')
    f  = cv2.getTrackbarPos('F','image')
    g1  = cv2.getTrackbarPos('G','image')
    h  = cv2.getTrackbarPos('H','image')
    i  = cv2.getTrackbarPos('I','image')
    j  = cv2.getTrackbarPos('J','image')
    k  = cv2.getTrackbarPos('K','image')
    l  = cv2.getTrackbarPos('L','image')
    m  = cv2.getTrackbarPos('M','image')
    n  = cv2.getTrackbarPos('N','image')
    o  = cv2.getTrackbarPos('O','image')
    r  = cv2.getTrackbarPos('C2','ED')
    s  = cv2.getTrackbarPos('D2','ED')

    
    img = cv2.imread('splitm1.jpg')
    img = cv2.resize(img,(600,600))

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


    # gray1T = np.ones((600,600),dtype ="uint8")
    # A1 = 0
    # for i in range(len(grayT)):
    #     for j in range(len(grayT)):
    #         A1 = grayT[i][j]
    #         gray1T[j][i] = A1

#    grayT = cv2.bitwise_not(grayT)
 #   edgesT = cv2.Canny(grayT,i,j)

    img1 = cv2.dilate(grayT,(5,5),iterations =2*o +1)
    img2 = cv2.bitwise_not(img1)
    img3 = cv2.dilate(img2,(5,5),iterations =2*o +1)

    cv2.imshow('img1',img1)
    cv2.imshow('img3',img3)
    cv2.imshow('img2',img2)
#    cv2.imshow('T7',T7)
    if cv2.waitKey(1) == 27:

        break

