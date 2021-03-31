import cv2
img = cv2.imread('test.jpg')
original_img = img

B = original_img[:,:,0]
G = original_img[:,:,1]
R = original_img[:,:,2]

B_equ = cv2.equalizeHist(B)
G_equ = cv2.equalizeHist(G)
R_equ = cv2.equalizeHist(R)

original_img[:,:,0] = B_equ
original_img[:,:,1] = G_equ
original_img[:,:,2] = R_equ 

re_size = cv2.resize (original_img,(1500,900))
cv2.imshow('show',re_size)
cv2.waitKey(0)