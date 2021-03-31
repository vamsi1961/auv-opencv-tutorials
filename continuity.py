import cv2
import numpy as np
import time


start = time.time()

def func1(array):
    count = 0
    array1 =[]
    array = np.append(array,0)
#    a = np.arange(len(array)-1)
    for i in range(len(array)-1):
        if (array[i] == 255):
            count = count + 1
 #           print(count)
            
            if (array[i+1] != 255):
                array1 = np.append(array1,count)
                count = 0
 #   print(array)   
 #   print(array1)         
     
#    print(array1)
#    print(max)

    return(array1)   


def func2(array):
 #   print(array)
    v =0

    max = array[0]
    for v in range(len(array)):
        if(array[v] >  max):
            max = array[v]
    return max  

def func(array):
    count = 0
    array1 =[]
    array = np.append(array,0)
#    a = np.arange(len(array)-1)
    for i in range(len(array)-1):
        if (array[i] == 255):
            count = count + 1
 #           print(count)
            
            if (array[i+1] != 255):
                array1 = np.append(array1,count)
                count = 0
 #   print(array)   
 #   print(array1)         
     
#    print(array1)
#    print(max)
    return(array1)   
#    print(thresh)

img =cv2.imread("f2.jpg")
array = cv2.resize(img,(600,600))
gray = cv2.cvtColor(array,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
#print(thresh)

#print(index)

maximum = []
array2 = np.ones((600,600),dtype ="uint8")
k =0
i = 0
j = 0 
k1 = 0
k = 0
for i in range(len(thresh[0])):
    for j in range(len(thresh[0])):
        k1 = thresh[j][i]
        array2[i][j] = k1
 #       print(k1)
#    print(thresh)
#    print(array2)
#    print(array2.shape)
#print(array2)
for k in range(600): 
    
    max = []
    maxim = 0

    array = array2[k]
#    print(array[90])
    max =func(array2[k])

 #   print(array2[k])
#        print(max)
    maxim = func2(max)
    maximum = np.append(maximum,maxim)
#    print(maximum)


max1 = np.amax(maximum) 
#    print(max1)

for i1 in range(len(maximum)):    
    if(maximum[i1] == max1):
        break

#print(i1)        
thresh1 = np.copy(thresh)
k = i1
for i in range(600):
    thresh[i][k] =0
    thresh[i][k+1] =0
    thresh[i][k+2] =0
    thresh[i][k+3] =0
    thresh[i][k+4] =0
    thresh[i][k+5] =0
    thresh[i][k-1] =0
    thresh[i][k-2] =0
    thresh[i][k-3] =0
    thresh[i][k-4] =0
    
#     thresh[i][k-5] =0
# thresh[:,i+5:] = 0
# thresh1[:,i-5:i+5] = 0

maximum1 = []
array2 = np.ones((600,600),dtype ="uint8")
k =0
i = 0
j = 0 
k1 = 0
k = 0
for i in range(len(thresh[0])):
    for j in range(len(thresh[0])):
        k1 = thresh[j][i]
        array2[i][j] = k1
   #     print(k1)
#    print(thresh)
#    print(array2)
#    print(array2.shape)

k = 0
for k in range(600): 
    print(k)
    array = []
    max1 = []
    maxim1 = 0
    maximum1 =[]
    array = array2[k]
    print(array)
    array[300] = 255
#    print(array[599])
#    print(len(array))    
    
    

    max1 = func(array)
    print(max)
    maxim1 = func2(max1)
#    print(maxim)

    maximum1 = np.append(maximum1,max1)
#    print(maximum)


max11 = np.amax(maximum1) 
#print(max11)
i =0
print(len(maximum1))
for i in range(len(maximum1)):    
    if(maximum1[i] == max11):
        break
 
#print(i)
k = i
j =0
for j in range(600):

    thresh[j][k] =0
    thresh[j][k+1] =0
    thresh[j][k+2] =0
    thresh[j][k+3] =0
    thresh[j][k+4] =0
    thresh[j][k+5] =0
    thresh[j][k-1] =0
    thresh[j][k-2] =0
    thresh[j][k-3] =0
    thresh[j][k-4] =0


cv2.imshow("img",img)
cv2.imshow("thresh1",thresh1)
stop = time.time() - start
print(stop)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)



