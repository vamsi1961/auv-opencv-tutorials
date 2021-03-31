# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np 
import math
#from matplotlib import pyplot as plt


a=0
b=0


def nothing(x):
    pass

cv2.namedWindow('image')

cap = cv2.VideoCapture(0)

cv2.createTrackbar('Hlo','image',4,255,nothing)
cv2.createTrackbar('Hup','image',20,255,nothing)
cv2.createTrackbar('Slo','image',144,255,nothing)
cv2.createTrackbar('Sup','image',255,255,nothing)
cv2.createTrackbar('Vlo','image',126,255,nothing)
cv2.createTrackbar('Vup','image',255,255,nothing)


# load the image, convert it to grayscale, blur it slightly,
# and threshold it

while(1) :




    _, frame = cap.read() 

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    Hlo = cv2.getTrackbarPos('Hlo','image')
    Hup = cv2.getTrackbarPos('Hup','image')
    Slo = cv2.getTrackbarPos('Slo','image')
    Sup = cv2.getTrackbarPos('Sup','image') 
    Vlo = cv2.getTrackbarPos('Vlo','image')
    Vup = cv2.getTrackbarPos('Vup','image')


    low = np.array([Hlo,Slo,Vlo])
    high = np.array([Hup,Sup,Vup])

    
    #thresh = cv2.threshold(gray_image,127,255,0)
    frame_mask = cv2.inRange(hsv,low,high)
    output = cv2.bitwise_and(frame,frame, mask = frame_mask)
    gray_image = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    # find contours in the thresholded image
    cnts = cv2.findContours(frame_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    # loop over the contours
    for c in cnts:

      
	   M = cv2.moments(gray_image)
      
	   a = int(M["m10"] / M["m00"])
      
	   b = int(M["m01"] / M["m00"])
     
   
	   cv2.drawContours(output,[c], -1, (0, 255, 0), 2)
    cv2.circle(output, (a, b), 1, (255, 255, 255), -1)
    cv2.putText(output, "centroid", (a - 25, b - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	#cv2.imshow("Image", output)
   # show the image
	 
    #plt.imshow(frame, cmap = 'gray', interpolation = 'bicubic')
    cv2.imshow("frame mask",frame_mask)
    cv2.imshow("original webcame feed",frame)
    cv2.imshow("Color Tracking",output)
    #plt.show()
    #cv2.imshow("Centre", frame)
 #   print(cX)	
    if cv2.waitKey(1) == 27:
         break

cv2.destroyAllWindows()
cap.release()







	