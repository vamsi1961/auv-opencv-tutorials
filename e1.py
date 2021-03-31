import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow('Trackbars')


cv2.createTrackbar('K','Trackbars',1,10,nothing)
cv2.createTrackbar('A','Trackbars',1,5,nothing)



while(1) :

    K = cv2.getTrackbarPos('K','Trackbars')
    A = cv2.getTrackbarPos('A','Trackbars')

    #image reading

    img = cv2.imread('test.jpg')
    img_re = cv2.resize(img,(60,60))
   
    #applying filters :Gaussian 

    blur = cv2.GaussianBlur(img_re,(2*K+1,2*K+1),cv2.BORDER_DEFAULT)

    #applying clahe 

    lab = cv2.cvtColor(blur, cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv2.merge(lab_planes)
    bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    #converting RGB to YCbCr

    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    imgYCC = cv2.cvtColor(rgb, cv2.COLOR_RGB2YCR_CB)
    
    #contrast stretching of Y
    Y_channel, Cr_channel, Cb_channel = cv2.split(imgYCC)
    # Create zeros array to store the stretched image
    # minmax_img = np.zeros((imgYCC.shape[0],imgYCC.shape[1]),dtype = 'uint8')
    minmax_img = np.copy(Y_channel)
    

    for i in range(60):
        for j in range(60):
            minmax_img[i,j] = 255*(Y_channel[i,j]-np.min(Y_channel))/(np.max(Y_channel)-np.min(Y_channel))
            


    
    merged_channels = cv2.merge((minmax_img,Cr_channel,Cb_channel))
    print(minmax_img.shape)
    median = cv2.medianBlur(merged_channels,5)
    lapl = cv2.Laplacian(median,cv2.CV_64F)

 #   img_rgb = cv2.cvtColor(lapl, cv2.COLOR_YCR_CB2RGB)

    
    cv2.imshow('RGB',lapl)
    

 
    if cv2.waitKey(0)== 27:
        break    

cv2.destroyAllWindows()