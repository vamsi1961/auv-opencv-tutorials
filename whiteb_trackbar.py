from __future__ import (division, absolute_import, print_function, unicode_literals)

import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('image')
# Insert any filename with path
img = cv.imread('test.jpg')

cv.createTrackbar('a','image',0,255,nothing)
cv.createTrackbar('b','image',1,255,nothing)
cv.createTrackbar('c','image',0,255,nothing)
cv.createTrackbar('d','image',1,255,nothing)

while (1):

    A = cv.getTrackbarPos('a','image')
    B = cv.getTrackbarPos('b','image')
    C = cv.getTrackbarPos('c','image')
    D = cv.getTrackbarPos('d','image')     


    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)

    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])

    r1 = np.arange(result.shape[0])   
    r2 = np.arange(result.shape[1])

    for x in np.nditer(r1):
       for y in np.nditer(r2):
            l, a, b = result[x, y, :]
            # fix for CV correction
            l *= 100 / 255.0
            result[x, y, 1] = a - ((avg_a -A ) * (l / B) * 1.1)
            result[x, y, 2] = b - ((avg_b -C) * (l / D) * 1.1)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
    
    cv.imshow('Temple', result)
    if cv.waitKey(1) == 27:
        break
#    cv.destroyAllWindows()