import cv2
import numpy as np

im = cv2.imread("sauvc.png")
img = cv2.resize(im,(600,600))


def nothing(x):
    pass


cv2.namedWindow('Trackbars')
cv2.createTrackbar('A','Trackbars',0,100,nothing)

while(1) :

    a = cv2.getTrackbarPos('A','Trackbars')


    BGR = cv2.split(img)

    BGR[0] = (BGR[0] * a/100)

    bgr = cv2.merge((BGR[0],BGR[1],BGR[2]))

    cv2.imshow("bgr",bgr)
    cv2.imshow("BGR",img)
    if cv2.waitKey(1) == 27:
        break


