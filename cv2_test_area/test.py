import cv2 as cv2
import numpy as np

img = cv2.imread('/home/alex/inzynierka/cv2_test_area/img/kostka.jpg')

med_val = np.median(img)

img_k9 = cv2.blur(img, ksize = (9, 9))

lower = int(max(0, .7*med_val))
upper = int(min(255, 1.3*med_val))

edges_k9 = cv2.Canny(img_k9, lower, upper)

edges = cv2.Canny(image=img, threshold1=127, threshold2=127)


img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
dst = cv2.cornerHarris(img_gray, blockSize = 2, ksize = 3, k = .04)
img_2 = img.copy()
img_2[dst>0.01*dst.max()]=[255,0,0]


imgray = cv2.cvtColor(img_k9,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
ctr = np.zeros(img.shape, dtype=np.uint8)
cv2.drawContours(ctr, contours, -1, (0,255,0), 3)
img_with_contours = img.copy()
cv2.drawContours(img_with_contours, contours, -1, (0,255,0), 3)



cv2.imshow('image1', img[:,:,::-1]) 
cv2.imshow('image2', thresh) 
cv2.imshow('image3', ctr[:,:,::-1]) 
cv2.imshow('image4', img_with_contours[:,:,::-1]) 

cv2.waitKey(0)  
  
#closing all open windows  
cv2.destroyAllWindows()  