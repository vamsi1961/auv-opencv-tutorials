import cv2
import numpy as np
from collections import Counter 
  
def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0] 
    

array1 = []
array = []
array2 = []
im = cv2.imread('final.jpg')
print(im.shape) 
img = cv2.resize(im,(600,600))  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]
for i in range(len(thresh[0])):
    for j in range(len(thresh[0])):
        if thresh[i][j] == 255:
          
           array = np.append(array,j)  
print(array)
k = most_frequent(array)
# array2 = np.delete(array,k)
# k1 = most_frequent(array2)
# print(k1)
#print(k)
result = []

for i in range(len(thresh[0])):
    for j in range(len(thresh[0])):
        if thresh[i][j] == 255:
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
           
print(result)
for i in range(len(result)):
     image[result[i][0]][result[i][1]]  = 255                          
cv2.imshow("image",image) 
cv2.imwrite("poles2.jpg",image)                             
# print(image1[599][333])
cv2.waitKey(0)
