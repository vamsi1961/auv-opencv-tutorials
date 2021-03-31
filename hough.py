import cv2
import numpy as np

im = cv2.imread('auv1.jpg')
img = cv2.resize(im,(600,600))

def nothing(x):
    pass

cv2.namedWindow('FinalOutput')
cv2.createTrackbar('a','FinalOutput',0,1000,nothing)
cv2.createTrackbar('b','FinalOutput',0,1000,nothing)
cv2.createTrackbar('c','FinalOutput',0,1000,nothing)
cv2.createTrackbar('d','FinalOutput',0,10,nothing)

while 1 :

    A = cv2.getTrackbarPos('a','FinalOutput')
    B = cv2.getTrackbarPos('b','FinalOutput')
    C = cv2.getTrackbarPos('c','FinalOutput')
    D = cv2.getTrackbarPos('d','FinalOutput')

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,A,B,apertureSize = 3)
    minLineLength = C
    maxLineGap = D
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

        cv2.imshow("img",edges)
    if cv2.waitKey(1) == 27:
        cv2.imwrite("auv8.jpg",edges)
        break