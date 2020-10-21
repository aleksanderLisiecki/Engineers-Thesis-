import time
from cv2 import cv2

def make_a_photo(dev1 = "/dev/video0", dev2 = "/dev/video0"):
    frame_count = 8
    camera = cv2.VideoCapture(dev1) #change to video2
    time.sleep(0.1)
    for i in range(frame_count):
        return_value, image = camera.read()
    cv2.imwrite("img/cube_down_new.jpg", image)
    del(camera)

    camera = cv2.VideoCapture(dev2) #change to video4
    time.sleep(0.1)
    for i in range(frame_count):
        return_value, image = camera.read()
    cv2.imwrite("img/cube_up_new.jpg", image)
    del(camera)

