import numpy as np
import cv2
img1 = cv2.imread('tetris_block.png',1)
cv2.imshow('tetris_block.png',img1)
#img2 = cv2.imread('dogs.jpg',1)
#resize = cv2.resize(img2,(600,600))
#cv2.imshow('dogs.jpg',resize)
k = cv2.waitKey(0)
if k == 23:
 cv2.destroyAllWindows()
 print(img1)
 print(img2)
