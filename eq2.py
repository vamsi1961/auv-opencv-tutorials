import cv2
import numpy as np 

def nothing(x):
    pass
                                                                                            

cv2.namedWindow('Trackbars')

cv2.createTrackbar('L1','Trackbars',1,255,nothing)
cv2.createTrackbar('L0','Trackbars',1,255,nothing)
cv2.createTrackbar('L2','Trackbars',1,255,nothing)

cv2.createTrackbar('D1','weighted',1,100,nothing)
cv2.createTrackbar('P','Trackbars',1,255,nothing)
cv2.createTrackbar('O','Trackbars',1,255,nothing)

while (1):

    L0 = cv2.getTrackbarPos('L0','Trackbars')
    L1 = cv2.getTrackbarPos('L1','Trackbars')
    L2 =cv2.getTrackbarPos('L2','Trackbars')

    p = cv2.getTrackbarPos('P','Trackbars')    
    D1 = cv2.getTrackbarPos('D1','weighted')
    o=cv2.getTrackbarPos('O','Trackbars')

    img = cv2.imread('rod2.png')
    img_re = cv2.resize(img,(600,600))
    BGR = img_re
    

    B = img_re[:,:,0]
    G = img_re[:,:,1]
    R = img_re[:,:,2]

    B = cv2.equalizeHist(B)
    G = cv2.equalizeHist(G)
    R = cv2.equalizeHist(R)

    BGR[:,:,0] = B
    BGR[:,:,1] = G
    BGR[:,:,2] = R


    color_planes = cv2.split(img_re)
    planes=color_planes
    planes[0]=(color_planes[0])*(L0)
    planes[1]=(color_planes[1])*(L1)
    planes[2]=(color_planes[2])*(L2)

    lab = cv2.merge(planes)

    image = cv2.addWeighted(lab,D1/100.0,BGR,(1-(D1/100.0))
    
    grayT = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    edgesT = cv2.Canny(grayT,i,j,apertureSize = 3)
    img2 = cv2.erode(edgesT,(5,5),iterations = 2*p +1)
    img1 = cv2.dilate(img2,(5,5),iterations =2*o +1)

    cv2.imshow("image",image)
    cv2.imshow("img1",img1)

    if cv2.waitKey(1) == 27:
        break


