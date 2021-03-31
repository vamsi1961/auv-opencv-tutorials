import cv2
img = cv2.imread('rod.jpg')
white = white_balance_loops(img)
cv2.imshow('white_bal_img',white)