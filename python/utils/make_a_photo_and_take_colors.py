import time
from cv2 import cv2

PATH = '/home/pi/inzynierka/img/cube_photos'


def make_a_photo_and_take_colors(coords_down, coords_up, cam_down, cam_up, number = 0):
    frame_count = 1
    def capture(dev, destination, frame_count, coords, camera):
        photo_ready = False
        # camera = cv2.VideoCapture(dev) 
        # time.sleep(0.1)
        image = None
        for i in range(frame_count):
            return_value, image = camera.read()
        
        colors = []
        for i in range(0, len(coords), 2):
            pix = image[coords[i+1], coords[i]]
            colors.append((int(pix[2]),int(pix[1]),int(pix[0])))

        # file_location = PATH+"/cube_"+destination+"_"+str(number)+".png"
        # photo_ready = cv2.imwrite(file_location, image)

        # del(camera)
        return colors
    
    colors_down = capture(cam_down, 'down', 8, coords_down, cam_down)   #change to video2
    colors_up = capture(cam_up, 'up', 8, coords_up, cam_up)   #change to video4
    return (colors_down + colors_up)
    