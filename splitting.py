import cv2
import numpy as np


def nothing(x):
    pass

cv2.namedWindow('FinalOutput')
cv2.createTrackbar('a','FinalOutput',0,500,nothing)
cv2.createTrackbar('b','FinalOutput',0,500,nothing)

while 1:


    A = cv2.getTrackbarPos('a','FinalOutput')
    B = cv2.getTrackbarPos('b','FinalOutput')
    img = cv2.imread('AUV3.jpg')
    edges = cv2.Canny(img,A,B)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()

    cv2.imshow("canny",edges)
    cv2.waitKey(1)