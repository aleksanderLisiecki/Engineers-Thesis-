import time
from cv2 import cv2

PATH = '/home/pi/inzynierka/img/cube_photos'


def make_a_photo_and_take_colors(coords_down, coords_up, cam_down = "/dev/video0", cam_up = "/dev/video0", number = 0):
    frame_count = 8
    def capture(dev, destination, frame_count, coords):
        photo_ready = False
        camera = cv2.VideoCapture(dev) 
        time.sleep(0.1)
        image = None
        for i in range(frame_count):
            return_value, image = camera.read()
        
        colors = []
        for i in range(0, len(coords), 2):
            pix = image[coords[i+1], coords[i]]
            colors.append((pix[2],pix[1],pix[0]))
        del(camera)
        return colors
    
    colors_down = capture(cam_down, 'down', 8, coords_down)   #change to video2
    colors_up = capture(cam_up, 'up', 8, coords_up)   #change to video4
    return (colors_down + colors_up)
    