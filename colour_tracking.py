import cv2
import numpy as np 
import imutils
import math

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

while(1) :
    _, frame = cap.read() 
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    Hlo = cv2.getTrackbarPos('Hlo','image')
    Hup = cv2.getTrackbarPos('Hup','image')
    Slo = cv2.getTrackbarPos('Slo','image')
    Sup = cv2.getTrackbarPos('Sup','image') 
    Vlo = cv2.getTrackbarPos('Vlo','image')
    Vup = cv2.getTrackbarPos('Vup','image')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low = np.array([Hlo,Slo,Vlo])
    high = np.array([Hup,Sup,Vup])

    frame_mask = cv2.inRange(hsv,low,high)
    output = cv2.bitwise_and(frame,frame, mask = frame_mask)

    #res2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    M = moments(frame_mask)

#    cX = int(M["m10"] / M["m00"])
#    cY = int(M["m01"] / M["m00"])
  
#    cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
#    cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
    
    cv2.imshow("frame mask",frame_mask)
    cv2.imshow("original webcame feed",frame)
    cv2.imshow("Color Tracking",output) 




    if cv2.waitKey(1) == 27:
         break

cv2.destroyAllWindows()
cap.release()


     
     
