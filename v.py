import cv2
import numpy as np 


def nothing(x):
    pass

cv2.namedWindow('image')


cv2.createTrackbar('Hlo','image',136,255,nothing)
cv2.createTrackbar('lo','image',72,255,nothing)

while 1 :
    A  = cv2.getTrackbarPos('Hlo','image')
    B  = cv2.getTrackbarPos('lo','image')
    img = cv2.imread('test.jpg')

    img_re = cv2.resize(img,(800,800))
    dst = cv2.fastNlMeansDenoisingColored(img_re,None,10,10,7,21)

    cv2.imshow('denoise',dst)
# Ycrcb = cv2.cvtColor(img_re,cv2.COLOR_BGR2LAB)
# b,g,r=cv2.split(img_re)
# B,G,R=list(map(cv2.equalizeHist,[b,g,r]))
# BGR=cv2.merge((B,G,R))


    blurT = cv2.bilateralFilter(img_re,9,75,75)

   # grayT = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
    # v = np.median(dst)
    # print(v)
    sigma = (A)/100
    kernel = np.ones((5,5), np.uint8)
#---- apply optimal Canny edge detection using the computed median----
    lower_thresh =40# int(max(0, (1.0 - sigma) * v))
    upper_thresh = 255#int(min(255, (1.0 + sigma) * v))
    edgesT = cv2.Canny(dst,upper_thresh,lower_thresh,apertureSize = 3)
    edgesT = cv2.dilate(edgesT,kernel,iterations = 1)
    # edges1 = cv2.Canny(dst,93,0,apertureSize = 3)
    # edges=cv2.Sobel(edgesT,cv2.CV_64F,1,0,ksize=7)

# ori = cv2.cvtColor(BGR,cv2.COLOR_LAB2BGR)

    cv2.imshow('image',edgesT)
# cv2.imshow('converted',ori)
    cv2.waitKey(20)