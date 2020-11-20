import time
from cv2 import cv2

PATH = '/home/pi/inzynierka/img/cube_photos'


def make_a_photo(cam_down = "/dev/video0", cam_up = "/dev/video0", number = 0):
    frame_count = 8
    def capture(dev, destination, frame_count):
        photo_ready = False
        while not photo_ready:
            camera = cv2.VideoCapture(dev) 
            time.sleep(0.1)
            for i in range(frame_count):
                return_value, image = camera.read()
            file_location = PATH+"/cube_"+destination+"_"+str(number)+".png"
            photo_ready = cv2.imwrite(file_location, image)
            del(camera)
    
    capture(cam_down, 'down', 8)   #change to video2
    capture(cam_up, 'up', 8)   #change to video4
    return True
    