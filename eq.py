import cv2
import numpy as np 

def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('C','image',0,100,nothing)
cv2.createTrackbar('D','image',0,100,nothing)

cv2.namedWindow('Trackbars')

cv2.createTrackbar('b','Trackbars',1,255,nothing)
cv2.createTrackbar('g','Trackbars',1,255,nothing)
cv2.createTrackbar('r','Trackbars',1,255,nothing)

cv2.createTrackbar('B','Trackbars',1,255,nothing)
cv2.createTrackbar('G','Trackbars',1,255,nothing)
cv2.createTrackbar('R','Trackbars',1,255,nothing)

cv2.createTrackbar('B1','Trackbars',1,255,nothing)
cv2.createTrackbar('G1','Trackbars',1,255,nothing)
cv2.createTrackbar('R1','Trackbars',1,255,nothing)

cv2.createTrackbar('P','Trackbars',1,25,nothing)
cv2.createTrackbar('O','Trackbars',1,25,nothing)


cv2.createTrackbar('I','im1',0,100,nothing)
cv2.createTrackbar('J','im1',0,100,nothing)

cv2.createTrackbar('K','im1',0,25,nothing)
cv2.createTrackbar('L','im1',0,25,nothing)
cv2.createTrackbar('M','im1',0,25,nothing)
cv2.createTrackbar('N','im1',0,25,nothing)

while(1) :
    
    c  = cv2.getTrackbarPos('C','image')
    d  = cv2.getTrackbarPos('D','image')

    A = cv2.getTrackbarPos('G','Trackbars')
    K = cv2.getTrackbarPos('B','Trackbars')
    Z = cv2.getTrackbarPos('R','Trackbars')

    
    A = cv2.getTrackbarPos('B','Trackbars')
    K = cv2.getTrackbarPos('G','Trackbars')
    Z = cv2.getTrackbarPos('R','Trackbars')

    x = cv2.getTrackbarPos('B1','Trackbars')
    Y = cv2.getTrackbarPos('G1','Trackbars')
    P = cv2.getTrackbarPos('R1','Trackbars')

    b = cv2.getTrackbarPos('b','Trackbars')
    g = cv2.getTrackbarPos('g','Trackbars')
    r = cv2.getTrackbarPos('r','Trackbars')


    i  = cv2.getTrackbarPos('I','im1')
    j  = cv2.getTrackbarPos('J','im1')
    k  = cv2.getTrackbarPos('K','im1')
    l  = cv2.getTrackbarPos('L','im1')
    m  = cv2.getTrackbarPos('M','im1')
    n  = cv2.getTrackbarPos('N','im1')

    p = cv2.getTrackbarPos('P','im1')
    o = cv2.getTrackbarPos('O','im1')

    image1 = cv2.imread('rod2.png')
    image2 = cv2.imread('splitm1.jpg')
    image_res1 = cv2.resize(image1,(600,600))
    image_res2 = cv2.resize(image2,(600,600))
    b,g,r=cv2.split(image_res1)
    B,G,R=list(map(cv2.equalizeHist,[b,g,r]))
    BGR=cv2.merge((B,G,R))


    img = cv2.cvtColor(image_res2, cv2.COLOR_BGR2LUV)

    color_planes = cv2.split(img)
    planes=color_planes
    
    planes[0]=(color_planes[0]-b)*(A/X)
    planes[1]=(color_planes[1]-g)*(K/Y)
    planes[2]=(color_planes[2]-r)*(Z/P)

    lab = cv2.merge(planes)
   
    T = cv2.addWeighted(BGR,c/100.0,lab,d/100.0,0)

    blurT = cv2.fastNlMeansDenoisingColored(T,None,k,l,m,n)
    grayT = cv2.cvtColor(blurT,cv2.COLOR_BGR2GRAY)
    edgesT = cv2.Canny(grayT,i,j,apertureSize = 3)
    edgesC = cv2.erode(edgesT,(5,5),iterations = 2*p + 1)
    edgesD = cv2.dilate(edgesC,(5,5),iterations = 2*o + 1)
                                                                                                                                                                                                                                                                                                                                                                                        
    cv2.imshow('BGR',BGR)
    cv2.imshow('T',T)
    cv2.imshow('blurT',blurT)
    cv2.imshow('edgesT',edgesT)
    cv2.imshow('edgesC',edgesC)
    cv2.imshow('edgesD',edgesD)

        
    if cv2.waitKey(10)== 27:
        break    

