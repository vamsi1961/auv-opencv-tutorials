import cv2
import numpy as np
from collections import Counter 
from collections import Counter 

array1 = []
array = []
array2 = []
array3 =[]


def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0] 

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




    T1 = cv2.addWeighted(Bgr,0.38,bGr,0.0,0)
    T2 = cv2.addWeighted(BGr,0.0,bgR,0.0,0)
    T3 = cv2.addWeighted(BgR,0.1,bGR,0.02,0)
    T4 = cv2.addWeighted(T1,1,T2,1,0)
    T5 = cv2.addWeighted(T3,1,T4,1,0)
    T6 = cv2.addWeighted(T5,1,BGR,0.21,0)


    I1 = cv2.addWeighted(Bgr,0.38,bGr,0.0,0)
    I2 = cv2.addWeighted(BGr,0.0,bgR,0.0,0)
    I3 = cv2.addWeighted(BgR,0.10,bGR,0.02,0)
    I4 = cv2.addWeighted(I1,1,I2,1,0)
    I5 = cv2.addWeighted(I3,1,I4,1,0)
    I6 = cv2.addWeighted(I5,1,BGR,0.23,0)

    blurT = cv2.GaussianBlur(T6,(11,11),2)
    grayT = cv2.cvtColor(blurT,cv2.COLOR_BGR2GRAY)
    edgesT = cv2.Canny(grayT,91,0,apertureSize = 3)
    img1 = cv2.dilate(edgesT,None,iterations = 2)

    blurI = cv2.GaussianBlur(I6,(11,11),2)
    grayI = cv2.cvtColor(blurI,cv2.COLOR_BGR2GRAY)
    edgesI = cv2.Canny(grayI,26,64,apertureSize = 3)
    img2 = cv2.dilate(edgesI,None,iterations = 2)
    


    for i in range(len(img1[0])):
        for j in range(len(img1[0])):
            if img1[i][j] == 255:
          
                array = np.append(array,j)  
#print(array)
    k = most_frequent(array)
# array2 = np.delete(array,k)
# k1 = most_frequent(array2)
# print(k1)
#print(k)
    result = []

    for i in range(len(img1[0])):
        for j in range(len(img1[0])):
            if img1[i][j] == 255:
                if (k == j):
                    array1 = np.append(array1,i)
            #    print(i,j)
                image = np.zeros((600,600),np.uint8)
                image1 = np.copy(image)
                for a  in range(len(image1[0])): 
                    for b in range(len(image1[0])):
                        
                        if(a == i):
                            if(b == j):
                                image1[i][j] = 255
                                
                                
#                                print(image1[i,j])
                                result.append((i,j))
                                print("njkhk")
#print(result)
    for i in range(len(result)):
        image[result[i][0]][result[i][1]]  = 255   
        

    for i1 in range(len(img2[0])):
        for j1 in range(len(img2[0])):
            if img2[i1][j1] == 255:
          
                array2 = np.append(array2,j1)  
#print(array2)
    k1 = most_frequent(array2)
# array2 = np.delete(array,k)
# k1 = most_frequent(array2)
# print(k1)
#print(k)
    result2 = []

    for i1 in range(len(img2[0])):
        for j1 in range(len(img2[0])):
            if img2[i1][j1] == 255:
                if (k1 == j1):
                    array3 = np.append(array3,i1)
            #    print(i,j)
                    image2 = np.zeros((600,600),np.uint8)
                    image3 = np.copy(image2)
                    for a1  in range(len(image3[0])): 
                        for b1 in range(len(image3[0])):
                            if(a1 == i1):
                                if(b1 == j1):
                                    image3[i1][j1] = 255
                                
#                                print(image1[i,j])
                                    result2.append((i1,j1))
           
#print(result2)
    for i in range(len(result2)):
        image2[result2[i][0]][result2[i][1]]  = 255  

    finalimage = cv2.bitwise_or(image,image2) 
    cv2.imshow("finalimage",finalimage)
    if cv2.waitKey(1)== 27 :
        break
    

# cv2.imshow("image",image)
# cv2.imshow("image2",image2) 
# cv2.imshow("im",im)

# cv2.imshow("BGR",BGR)
c
    