import cv2
img = cv2.imread('tetris_block.png',0)
while 1:
 cv2.imshow('tetris_block.png',img)
 k = cv2.waitKey(0)
 print(k)

 if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    break
 
 elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('tetris.jpg',img)
    cv2.destroyAllWindows()
    break