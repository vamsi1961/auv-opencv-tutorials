from __future__ import(division,absolute_import,print_function,unicode_literals)
import cv2
import numpy as np

def nothing(x):
    pass

# cv2.namedWindow('image')
cv2.namedWindow('white')

im = cv2.imread('test.jpg')
img = cv2.resize(im,(500,500))   

b,g,r=cv2.split(img)
B,G,R=list(map(cv2.equalizeHist,[b,g,r]))

cv2.createTrackbar('x','white',0,255,nothing)
cv2.createTrackbar('y','white',1,255,nothing)
cv2.createTrackbar('z','white',0,255,nothing)
cv2.createTrackbar('w','white',1,255,nothing)


Bgr=cv2.merge((B,g,r))
bGr=cv2.merge((b,G,r))
bgR=cv2.merge((b,g,R))
BGr=cv2.merge((B,G,r))
BgR=cv2.merge((B,g,R))
bGR=cv2.merge((b,G,R))
BGR=cv2.merge((B,G,R))

# cv2.createTrackbar('a','image',0,100,nothing)
# cv2.createTrackbar('b','image',0,100,nothing)
# cv2.createTrackbar('c','image',0,100,nothing)
# cv2.createTrackbar('d','image',0,100,nothing)
# cv2.createTrackbar('e','image',0,100,nothing)
# cv2.createTrackbar('f','image',0,100,nothing)
# cv2.createTrackbar('k','image',11,100,nothing)
# cv2.createTrackbar('l','image',0,100,nothing)
# cv2.createTrackbar('m','image',0,100,nothing)



while(1) :

    # A = cv2.getTrackbarPos('a','image')
    # B = cv2.getTrackbarPos('b','image')
    # C = cv2.getTrackbarPos('c','image')
    # D = cv2.getTrackbarPos('d','image') 
    # E = cv2.getTrackbarPos('e','image')
    # F = cv2.getTrackbarPos('f','image')
    # K = cv2.getTrackbarPos('k','image')
    # L = cv2.getTrackbarPos('l','image')
    # M = cv2.getTrackbarPos('m','image')

    X = cv2.getTrackbarPos('x','white')
    Y = cv2.getTrackbarPos('y','white')
    Z = cv2.getTrackbarPos('z','white')
    W = cv2.getTrackbarPos('w','white')

    result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    r1 = np.arange(result.shape[0])   
    r2 = np.arange(result.shape[1])

    for x in np.nditer(r1):
       for y in np.nditer(r2):
            l, a, b = result[x, y, :]
                # fix for CV correction
            l *= 100 / 255
            result[x, y, 1] = a - ((avg_a - X ) * (l / Y) * 1.1)
            result[x, y, 2] = b - ((avg_b - Z) * (l / W) * 1.1)
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    
    cv2.imshow('final',result)   

   
    # T1 = cv2.addWeighted(Bgr,(A/100.),BGr,(B/100.),0)
    # T2 = cv2.addWeighted(bGr,(C/100.),bgR,(D/100.),0)
    # T3 = cv2.addWeighted(BgR,(E/100.),bGR,(F/100.),0)
    # T4 = cv2.addWeighted(T1,1,T2,1,0)
    # T5 = cv2.addWeighted(T4,1,T3,1,0)
    # T6 = cv2.addWeighted(BGR,1,T5,1,0)

    # blurT = cv2.GaussianBlur(T6,(K,K),2,2,cv2.BORDER_DEFAULT)
    # grayT = cv2.cvtColor(blurT,cv2.COLOR_BGR2GRAY)
    # edgesT = cv2.Canny(grayT,L,M,apertureSize = 3)
    # img1 = cv2.dilate(edgesT,None,iterations = 2)
    
    #cv2.imshow('img',img1)
    # img2=np.copy(img1)
    # x=np.uint8(img1==255)
    # summa=np.sum(x,axis=0)

    # one=np.amax(summa)
    # one_index=np.argmax(summa)
    # print(summa)

    # summa1=np.copy(summa)
    # summa1[one_index-5:one_index+5]=0
    # two=np.amax(summa1)
    # two_index=np.argmax(summa1)

    # img1[:,0:one_index-5]=img1[:,one_index+5:two_index-5]=img1[:,two_index+5:]=0

    # print(one,one_index,two,two_index)

    # now = time.time() - start
    # print(now) 
    # cv2.imshow('image1',img2)
    # cv2.imshow('image',img1)
    if cv2.waitKey(1)== 27:
        break