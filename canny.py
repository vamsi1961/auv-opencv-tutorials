
import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('rod.jpg')
img = cv2.resize(im,(800,800))   


def nothing(x):
    pass

cv2.namedWindow('FinalOutput')
cv2.createTrackbar('a','FinalOutput',0,100,nothing)
cv2.createTrackbar('b','FinalOutput',0,100,nothing)
cv2.createTrackbar('c','FinalOutput',0,100,nothing)
cv2.createTrackbar('d','FinalOutput',0,100,nothing)
cv2.createTrackbar('e','FinalOutput',0,100,nothing)
cv2.createTrackbar('f','FinalOutput',0,100,nothing)
cv2.createTrackbar('g','FinalOutput',0,100,nothing)
cv2.createTrackbar('h','FinalOutput',0,100,nothing)
cv2.createTrackbar('i','FinalOutput',0,100,nothing)

bgr=np.copy(img)
Bgr=np.copy(img)
bGr=np.copy(img)
bgR=np.copy(img)
BGr=np.copy(img)
BgR = np.copy(img)
bGR = np.copy(img)
BGR=np.copy(img)

B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]

B_equ = cv2.equalizeHist(B)
G_equ = cv2.equalizeHist(G)
R_equ = cv2.equalizeHist(R)

while(1) :
    Bgr[:,:,0] = B_equ
    bGr[:,:,1] = G_equ
    bgR[:,:,2] = R_equ
    BGr[:,:,0] = B_equ
    BGr[:,:,1] = G_equ
    bGR[:,:,1] = G_equ
    bGR[:,:,1] = R_equ
    BgR[:,:,0] = B_equ
    BgR[:,:,2] = R_equ
    BGR[:,:,0] = B_equ
    BGR[:,:,1] = G_equ
    BGR[:,:,2] = R_equ

    TA = cv2.getTrackbarPos('a','FinalOutput')
    TB = cv2.getTrackbarPos('b','FinalOutput')
    TC = cv2.getTrackbarPos('c','FinalOutput')
    TD = cv2.getTrackbarPos('d','FinalOutput') 
    TE = cv2.getTrackbarPos('e','FinalOutput')
    TF = cv2.getTrackbarPos('f','FinalOutput')
    TG = cv2.getTrackbarPos('g','FinalOutput')
    TH = cv2.getTrackbarPos('h','FinalOutput')
    TI = cv2.getTrackbarPos('i','FinalOutput')

    I1 = cv2.addWeighted(Bgr,TA/100.0,bGr,TB/100.0,0)
    I2 = cv2.addWeighted(BGr,TC/100.0,bgR,TD/100.0,0)
    I3 = cv2.addWeighted(BgR,TE/100.0,bGR,TF/100.0,0)
    I4 = cv2.addWeighted(I1,1,I2,1,0)
    I5 = cv2.addWeighted(I3,1,I4,1,0)
    I6 = cv2.addWeighted(I5,1,BGR,TG/100.0,0)

    blur = cv2.GaussianBlur(I6,(11,11),TF)
    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,TH,TI,apertureSize = 3)
    img_dialated = cv2.dilate(edges,None,iterations = 2)

    cv2.imshow("image",img_dialated)
 #   print(img_dilated.shape)
 #   print(img_dialated.shape)
    if cv2.waitKey(1)== 27 :
#        cv2.imwrite("f2.jpg",img_dialated)

        break 

