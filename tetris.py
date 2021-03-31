# import the necessary packages
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
    help= "path to  image")
args = vars(ap.parse_args())

# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
#image = cv2.imread(args["image"])
#cv2.imshow("Image", image)

 
# convert the image to grayscale
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray", gray)
#cv2.waitKey(0)	

# applying edge detection we can find the outlines of objects in
# images
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
