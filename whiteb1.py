from __future__ import (
    division, absolute_import, print_function, unicode_literals)

import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('FinalOutput')
cv.createTrackbar('a','FinalOutput',0,255,nothing)
cv.createTrackbar('b','FinalOutput',0,255,nothing)
cv.createTrackbar('c','FinalOutput',1,255,nothing)
cv.createTrackbar('d','FinalOutput',1,255,nothing)

def show(final):
    print('display')
    


# Insert any filename with path

def white_balance_loops(img):
    A = cv.getTrackbarPos('a','FinalOutput')
    B = cv.getTrackbarPos('b','FinalOutput')
    C = cv.getTrackbarPos('c','FinalOutput')
    D = cv.getTrackbarPos('d','FinalOutput') 
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    for x in range(result.shape[0]):
        for y in range(result.shape[1]):
            l, a, b = result[x, y, :]
            # fix for CV correction
            l *= 100 / 255.0
            print(A,B,C,D)
            result[x, y, 1] = a - ((avg_a - A) * (l / (C*1.0)) * 1.1)
            result[x, y, 2] = b - ((avg_b - B) * (l / (D*1.0)) * 1.1)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
    cv.imshow('Temple', result)
    if cv.waitKey(20)==ord('s'):
        cv.imwrite("whitebalanced.jpg",result)
    return result

while(1) :
    img = cv.imread('test.jpg')
    img = cv.resize(img,(600,600))
    x=np.hstack((img, white_balance_loops(img)))
   