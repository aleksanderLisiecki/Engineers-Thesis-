import cv2 as cv2
import argparse
import imutils

# Load the image
image = cv2.imread('/home/alex/inzynierka/cv2_test_area/img/kostka.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 75, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	# show the image
	cv2.imshow("Image", image)
    

cv2.imshow('image1', thresh) 
# cv2.imshow('image2', thresh) 
# cv2.imshow('image3', ctr[:,:,::-1]) 
# cv2.imshow('image4', img_with_contours[:,:,::-1]) 

cv2.waitKey(0)  
  
#closing all open windows  
cv2.destroyAllWindows()  