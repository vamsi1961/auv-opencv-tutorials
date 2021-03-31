import cv2
import numpy as np


cap = cv2.VideoCapture('auv.mp4') 
frame_counter = 0
while(True):
    # Capture frame-by-frame
    ret, im = cap.read()
    frame_counter += 1
    #If the last frame is reached, reset the capture and the frame_counter
    if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0 #Or whatever as long as it is the same as next line
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    img = cv2.resize(im,(800,800))   
    img1 = cv2.resize(im,(900,900))

    cv2.imshow("img",img)
    cv2.imshow("img1",img1)
    if cv2.waitKey(1)== 27 :
        break