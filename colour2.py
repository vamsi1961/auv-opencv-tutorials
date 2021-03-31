import cv2
import numpy as np 
import imutils


def nothing(x):
    pass


img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

#cv2.namedWindow('image')

cap = cv2.VideoCapture(0)

cv2.createTrackbar('Hlo','image',4,255,nothing)
cv2.createTrackbar('Hlo','image',4,255,nothing)
cv2.createTrackbar('Hlo','image',4,255,nothing)
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)


while(1) :
    frame = cap.read() 

    r = cv2.getTrackbarPos('Hlo','image')
    g = cv2.getTrackbarPos('Hup','image')
    b = cv2.getTrackbarPos('Slo','image')