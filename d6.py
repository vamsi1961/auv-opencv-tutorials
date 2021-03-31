import cv2
import numpy as np


def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('A','image',1,100,nothing)


while(1) :

    a  = cv2.getTrackbarPos('A','image')


    img = cv2.imread("rod2.png")
    img = cv2.resize(img,(600,600))

    B,G,R = cv2.split(img)
    B = B/a
    
    BGR=cv2.merge((B,G,R))
    cv2.imshow("image",BGR)
    cv2.waitKey(1)