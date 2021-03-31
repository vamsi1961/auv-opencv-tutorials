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

    return(array1)   


def func2(array):
#    print(array)
    v =0

    max = array[0]
    for v in range(len(array)):
        if(array[v] >  max):
            max = array[v]
    return max  

def func(array):
#    print(array)
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
        
     
#    print(array1)


    return(array1)   
img =cv2.imread("f2.jpg")
array = cv2.resize(img,(600,600))
gray = cv2.cvtColor(array,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)


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

for k in range(600): 
#    print(k)
    array = array2[k]
    maxim = 0
#    print(array2[k])
#    print(array)
    array[599] = 255
    max =func(array)

    maxim = func2(max)

    
    maximum = np.append(maximum,maxim)
#    print(maximum)


max1 = np.amax(maximum) 
#    print(max1)

for i1 in range(len(maximum)):    
    if(maximum[i1] == max1):
        break

#print(i1)        
# thresh1 = np.copy(thresh)
k = i1
thresh2 = np.zeros((600,600),dtype ="uint8")

# thresh[:,i+5:] = 0
thresh[:,k-5:k+5] = 0
thresh2[:,k-5:k+5] = 255

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

for k in range(600): 

    array = array2[k]
    maxim = 0

#    print(array)
    array[599] = 255
    max =func(array)

    maxim = func2(max)
  
    maximum = np.append(maximum,maxim)

max1 = np.amax(maximum) 


for i1 in range(len(maximum)):    
    if(maximum[i1] == max1):
        break


k =i1
thresh2[:,k-5:k+5] = 255

# cv2.imshow("img",img)
cv2.imshow("thresh1",thresh2)
stop = time.time() - start
print(stop)
# cv2.imshow("thresh",thresh)
cv2.waitKey(0)



