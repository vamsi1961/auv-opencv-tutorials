import cv2
import numpy as np

img = np.ones((500,500,3),np.uint8)
img2 = np.ones((500,500,3),np.uint8)
for i in range(200):
    img2[i,500,3] = (255,255,255)
    
cv2.imshow("img",img)
cv2.imshow("img2",img2)
cv2.waitKey(0)
