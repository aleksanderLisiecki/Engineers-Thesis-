import time
from cv2 import cv2

def make_a_photo(dev1 = "/dev/video0", dev2 = "/dev/video0"):
    frame_count = 8
    def capture(dev, destination, frame_count):
        photo_ready = False
        while not photo_ready:
            camera = cv2.VideoCapture(dev) 
            time.sleep(0.1)
            for i in range(frame_count):
                return_value, image = camera.read()
            photo_ready = cv2.imwrite("img/cube_"+destination+"_new.jpg", image)
            del(camera)
    
    capture(dev1, 'down', 8)   #change to video2
    capture(dev2, 'up', 8)   #change to video4
    return True
    