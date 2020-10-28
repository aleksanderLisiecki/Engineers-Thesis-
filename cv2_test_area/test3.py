import cv2
import numpy as np
# pylint: disable=maybe-no-member

image = cv2.imread('/home/alex/inzynierka/cv2_test_area/kostka.jpg')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

sensitivity = 100
lower_white = np.array([0, 0, 255 - sensitivity])
upper_white = np.array([255, sensitivity, 255])

mask = cv2.inRange(hsv, lower_white, upper_white)

image2 = image.copy()
image2[mask > 0] = (170, 170, 170)

x,y,w,h = 131,60,353,370
mask2 = np.zeros_like(image)
cv2.rectangle(mask2, (x,y), (x+w,y+h), (255, 255, 255), -1)

mask2_inv = 255 - mask2

image_masked = cv2.bitwise_and(image, mask2)

image2_masked = cv2.bitwise_and(image2, mask2_inv)

result = cv2.add(image_masked, image2_masked)



cv2.imshow('mask', mask)
cv2.imshow('image2', image2)
# cv2.imshow('mask2', mask2 )
# cv2.imshow('mask2_inv', mask2_inv)
cv2.imshow('image_masked', image_masked)
# cv2.imshow('image2_masked', image2_masked)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()