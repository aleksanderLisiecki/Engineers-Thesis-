import time
import cv2

frame_count = 8

camera = cv2.VideoCapture("/dev/video0") #change to video2
time.sleep(0.1)
for i in range(frame_count):
    return_value, image = camera.read()
cv2.imwrite("img/cube_down_new.jpg", image)
del(camera)

camera = cv2.VideoCapture("/dev/video0") #change to video4
time.sleep(0.1)
for i in range(frame_count):
    return_value, image = camera.read()
cv2.imwrite("img/cube_up_new.jpg", image)
del(camera)

