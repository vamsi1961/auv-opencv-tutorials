import cv2
import numpy as np 


img = cv2.imread('splitm.jpg')
img_re = cv2.resize(img,(600,600))

cv2.imshow('show',img_re)
    
cv2.waitKey(0)
    
