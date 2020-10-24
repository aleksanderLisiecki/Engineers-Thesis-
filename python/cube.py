#       |1 2 3|
#       |4 b 6|
#       |7 8 9|
# |1 2 3|1 2 3|1 2 3|1 2 3|
# |4 w 6|4 r 6|4 y 6|4 o 6|
# |7 8 9|7 8 9|7 8 9|7 8 9|
#       |1 2 3|
#       |4 g 6|
#       |7 8 9|
# https://roboticsbackend.com/raspberry-pi-master-arduino-slave-i2c-communication-with-wiringpi/
 

from PIL import Image, ImageDraw
from utils import read_points_from_file as read
from utils import colors
from utils import make_a_photo
from utils import history

class Cube:

    PATH = '/home/alex/inzynierka/'

    coords = [[],[]]
    coords_down = []
    coords_up = []

    colors = [[],[]]
    colors_down = []
    colors_up = []

    red_wall = [9]
    yellow_wall = [9]
    orange_wall = [9]
    white_wall = [9]
    blue_wall = [9]
    green_wall = [9]
    cube = [red_wall, yellow_wall, orange_wall, white_wall, blue_wall, green_wall]


    def __init__(self):
        
        self.read_points()  # get coords of the points 
        
        # self.make_photo() # save history and take a new photo
        self.take_colors()  # read colors from taken photo


    def read_points(self):
        self.coords = [self.coords_down, self.coords_up] = read.read_points_from_file(self.PATH + 'data/points.txt')

    def make_photo(self):
        history.save_history()
        make_a_photo.make_a_photo("/dev/video0", "/dev/video0")

    def take_colors(self):
        self.colors_down = colors.take_colors(self.coords_down, self.PATH + 'img/cube_down_new.jpg')
        self.olors_up = colors.take_colors(self.coords_down, self.PATH + 'img/cube_up_new.jpg')
        self.colors = [self.colors_down, self.colors_up]
