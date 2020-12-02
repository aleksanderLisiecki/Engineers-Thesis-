#           |37 38 39|
#           |40 b  42|
#           |43 44 45|
# | 1  2  3 |10 11 12|19 20 21|28 29 30|
# | 4  w  6 |13 r  15|22 y  24|31 o  33|
# | 7  8  9 |16 17 18|25 26 27|34 35 36|
#           |46 47 48|
#           |49 g  51|
#           |52 53 54| 


#! /usr/bin/python

import serial
import time
import random
import yaml

from PIL import Image, ImageDraw
from utils import points as read
from utils import take_colors
from utils import make_a_photo
from utils import make_a_photo_and_take_colors
from utils import history
from utils import draw_points_on_image

class Cube:

    PATH = '/home/pi/inzynierka/'

    coords = [[],[]]
    coords_down = []
    coords_up = []

    colors_on_photo = []
    colors_on_cube = []
    cube_transform = []

    cube = ['w']*9 + ['r']*9 + ['y']*9 + ['o']*9 + ['b']*9 + ['g']*9

    def __init__(self):
        
        self.coords = self.read_points()  # get coords of the points 
        ser = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=20)

        response = ""
        ser.write("connected?".encode())
        while response != "connected":
            response = self.wait_for_response(ser)


        timestr = time.strftime("%Y_%m_%d-%H_%M_%S")
        yaml_file_path = self.PATH+"data/yaml_files/"+"scrambles_"+timestr+".yaml"
        data = {}

        try:
            for key in range(25):
                self.cube, scramble = self.random_scramble(self.cube)

                print(key)
                
                data[key] = {}
                data[key]['scramble'] = scramble
                data[key]['colors'] = self.cube
                data[key]['collected_colors']={}

                
                scramble_cmd = ">"
                for s in scramble:
                    scramble_cmd += s
                print(scramble_cmd)
                ser.write(scramble_cmd.encode())
                response = ""
                while response != "done":
                    response = self.wait_for_response(ser)
                

                # while response != "button_pressed":
                #     response = self.wait_for_response(ser)


                ser.write("kalibracja".encode())
                response = ""
                while response != "done":
                    response = self.wait_for_response(ser)

                start = time.time()

                perms = ['NORMAL','R1O1','R2O2','R3O3', 0,'W1Y1','W2Y2','W3Y3', 0,'B1G1','B2G2','B3G3']
                commands = ['obrotRO', 'obrotWY', 'obrotBG']
                
                for i in range(len(perms)):                  
                    

                    if perms[i] != 0:
                        self.colors_on_photo = self.make_a_photo_and_take_colors(i) # take a new photo
                    else:
                        time.sleep(0.1)

                    
                    ser.write(commands[int((i)/4)].encode())
                    

                    if perms[i] != 0:
                        # self.colors_on_photo = self.take_colors(i)  # read colors from taken photo
                        self.colors_on_cube, self.cube_transform = self.assign_colors(self.colors_on_photo, perms[i])   # make an transformations of the perms
                        data[key]['collected_colors'][i] = self.colors_on_cube
                        # self.draw_cube(self.colors_on_cube, i)  # draw flat view of the photos
                        # self.draw_points_on_photo(i)

                    response = ""
                    while response != "done":
                        response = self.wait_for_response(ser)
                    response = ""
                        

                end = time.time()
                print("time: " + str(end - start))
        except:
            self.yaml_dump(yaml_file_path, data) 
            return  

            
        self.yaml_dump(yaml_file_path, data)   


        ser.write("wysrodkuj".encode())
        response = ""
        while response != "done":
            response = self.wait_for_response(ser)

        time.sleep(1)

        ser.write("wysrodkuj".encode())
        response = ""
        while response != "done":
            response = self.wait_for_response(ser)
        ser.write("wysrodkuj".encode())         




    def wait_for_response(self, ser):
        data = ""
        while ser.inWaiting():
                data = ser.readline()
                data = data.strip().decode()
                print(data)
        return data

    def read_points(self):
        [self.coords_down, self.coords_up] = read.read_points_from_file(self.PATH + 'data/points.txt')
        coords = self.coords_down + self.coords_up
        return coords

    def make_photo(self, number):
        return make_a_photo.make_a_photo("/dev/video2", "/dev/video0", number)

    def make_a_photo_and_take_colors(self, number):
        return make_a_photo_and_take_colors.make_a_photo_and_take_colors(self.coords_down, self.coords_up, "/dev/video2", "/dev/video0", number)

    def draw_points_on_photo(self, image_number):
        cube_transformation = self._transformations_table('NORMAL') 
        photo_transformation = self._transformations_table('PHOTO')
        draw_points_on_image.draw_points_on_image(self.coords_up, self.PATH + 'img/cube_photos/cube_up_'+str(image_number)+'.png', cube_transformation, photo_transformation, 'up')
        draw_points_on_image.draw_points_on_image(self.coords_down, self.PATH + 'img/cube_photos/cube_down_'+str(image_number)+'.png', cube_transformation, photo_transformation, 'down')

    def take_colors(self, image_number):
        """
        This function take an colors from photo in given points.
        """
        colors_down = take_colors.take_colors(self.coords_down, self.PATH + 'img/cube_photos/cube_down_'+str(image_number)+'.png')
        colors_up = take_colors.take_colors(self.coords_up, self.PATH + 'img/cube_photos/cube_up_'+str(image_number)+'.png')
        return (colors_down + colors_up)

    def assign_colors(self, colors_on_photo, rotation):
        """
        This function make an projection of read colors on given transformation of the cube.
        """
        cube_transformation = self._transformations_table(rotation)
        photo_transformation = self._transformations_table('PHOTO')
        projected_colors = [0] * 54
        for i in range(54):
            projected_colors[cube_transformation[i]-1] = colors_on_photo[photo_transformation[i]-1] if photo_transformation[i]!=0 else 0
        return  projected_colors, cube_transformation

    def draw_cube(self, colors, number=''):
        """
        This function draw an flat view of given colors.
        """
        cube_draw_points_x = [0,1,2,3,4,5,6,7,8,9,10,11,3,4,5,3,4,5]
        cube_draw_points_y = [3,4,5,3,4,5,3,4,5,3,4,5,0,1,2,6,7,8]
        im = Image.new(mode = "RGB", size = (480, 360), color = (255,255,255))
        draw = ImageDraw.Draw(im)
        n = 0
        for i in range(len(cube_draw_points_y)):
            y = cube_draw_points_y[i]
            for j in range(3):
                x = cube_draw_points_x[int(i/3)*3 + j]
                draw.rectangle(((x*40,y*40),((x*40)+40,(y*40)+40)), fill=(colors[n]), outline=(0,0,0), width=2)
                draw.text(((x*40)+16,(y*40)+16),fill=(100,100,100), text=str(self.cube_transform.index(n+1)+1))
                n+=1
        im.save(self.PATH+'img/flat_views/flat_view'+ str(number) +'.png')
        im.close()


    def random_scramble(self, cube):
        scramble = []
        random.seed()
        for i in range(10):
            scramble.append(random.choice('FBRLUD'))

        colors_after_scramble = cube[:]
        transformation_table = [0]*54

        for rotation in scramble:
            if rotation == 'F':
                transformation_table = self._transformations_table('R1')
            elif rotation == 'B':
                transformation_table = self._transformations_table('O1')
            elif rotation == 'R':
                transformation_table = self._transformations_table('Y1')
            elif rotation == 'L':
                transformation_table = self._transformations_table('W1')
            elif rotation == 'U':
                transformation_table = self._transformations_table('B1')
            elif rotation == 'D':
                transformation_table = self._transformations_table('G1')

            bufor = colors_after_scramble[:]
            for j in range(len(transformation_table)):
                colors_after_scramble[j] = bufor[transformation_table[j]-1]

        return colors_after_scramble, scramble

    def yaml_loader(self, filepath):
        with open(filepath, "r") as f:
            data = yaml.load(f, Loader= yaml.Loader)
        last_key_number = 0
        for key in data.keys():
            last_key_number = key
        return data, last_key_number
    def yaml_dump(self, filepath, data):
        with open(filepath, "w") as f:
            yaml.dump(data, f)


    def _transformations_table(self, t):
        """Choose wall color with: NORMAL, R, W, Y, O, B or G 
        NORMAL is an cube without any rotations.
        PHOTO means transformations of points on photos.
        Rotation of the wall choose by:
        - 1: 90deg clockwise, 
        - 2: 180deg, 
        - 3: 90deg counterclockwise
        e.g. R1 means that you rotate Red wall by 90 deg clockwise
        """
        return{
            'NORMAL': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54],
            'R1': [1,2,46,4,5,47,7,8,48,16,13,10,17,14,11,18,15,12,43,20,21,44,23,24,45,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,9,6,3,25,22,19,49,50,51,52,53,54],
            'R2': [1,2,25,4,5,22,7,8,19,18,17,16,15,14,13,12,11,10,9,20,21,6,23,24,3,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,48,47,46,45,44,43,49,50,51,52,53,54],
            'R3': [1,2,45,4,5,44,7,8,43,12,15,18,11,14,17,10,13,16,48,20,21,47,23,24,46,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,19,22,25,3,6,9,49,50,51,52,53,54],
            'W1': [7,4,1,8,5,2,9,6,3,37,11,12,40,14,15,43,17,18,19,20,21,22,23,24,25,26,27,28,29,52,31,32,49,34,35,46,36,38,39,33,41,42,30,44,45,10,47,48,13,50,51,16,53,54],
            'W2': [9,8,7,6,5,4,3,2,1,36,11,12,33,14,15,30,17,18,19,20,21,22,23,24,25,26,27,28,29,16,31,32,13,34,35,10,46,38,39,49,41,42,52,44,45,37,47,48,40,50,51,43,53,54],
            'W3': [3,6,9,2,5,8,1,4,7,46,11,12,49,14,15,52,17,18,19,20,21,22,23,24,25,26,27,28,29,43,31,32,40,34,35,37,10,38,39,13,41,42,16,44,45,36,47,48,33,50,51,30,53,54],
            'Y1': [1,2,3,4,5,6,7,8,9,10,11,48,13,14,51,16,17,54,25,22,19,26,23,20,27,24,21,45,29,30,42,32,33,39,35,36,37,38,12,40,41,15,43,44,18,46,47,34,49,50,31,52,53,28],
            'Y2': [1,2,3,4,5,6,7,8,9,10,11,34,13,14,31,16,17,28,27,26,25,24,23,22,21,20,19,18,29,30,15,32,33,12,35,36,37,38,48,40,41,51,43,44,54,46,47,39,49,50,42,52,53,45],
            'Y3': [1,2,3,4,5,6,7,8,9,10,11,39,13,14,42,16,17,45,21,24,27,20,23,26,19,22,25,54,29,30,51,32,33,48,35,36,37,38,34,40,41,31,43,44,28,46,47,12,49,50,15,52,53,18],
            'O1': [39,2,3,38,5,6,37,8,9,10,11,12,13,14,15,16,17,18,19,20,54,22,23,53,25,26,52,34,31,28,35,32,29,36,33,30,21,24,27,40,41,42,43,44,45,46,47,48,49,50,51,1,4,7],
            'O2': [27,2,3,24,5,6,21,8,9,10,11,12,13,14,15,16,17,18,19,20,7,22,23,4,25,26,1,36,35,34,33,32,31,30,29,28,54,53,52,40,41,42,43,44,45,46,47,48,49,50,51,39,38,37],
            'O3': [52,2,3,53,5,6,54,8,9,10,11,12,13,14,15,16,17,18,19,20,37,22,23,38,25,26,39,30,33,36,29,32,35,28,31,34,7,4,1,40,41,42,43,44,45,46,47,48,49,50,51,27,24,21],
            'B1': [10,11,12,4,5,6,7,8,9,19,20,21,13,14,15,16,17,18,28,29,30,22,23,24,25,26,27,1,2,3,31,32,33,34,35,36,43,40,37,44,41,38,45,42,39,46,47,48,49,50,51,52,53,54],
            'B2': [19,20,21,4,5,6,7,8,9,28,29,30,13,14,15,16,17,18,1,2,3,22,23,24,25,26,27,10,11,12,31,32,33,34,35,36,45,44,43,42,41,40,39,38,37,46,47,48,49,50,51,52,53,54],
            'B3': [28,29,30,4,5,6,7,8,9,1,2,3,13,14,15,16,17,18,10,11,12,22,23,24,25,26,27,19,20,21,31,32,33,34,35,36,39,42,45,38,41,44,37,40,43,46,47,48,49,50,51,52,53,54],
            'G1': [1,2,3,4,5,6,34,35,36,10,11,12,13,14,15,7,8,9,19,20,21,22,23,24,16,17,18,28,29,30,31,32,33,25,26,27,37,38,39,40,41,42,43,44,45,52,49,46,53,50,47,54,51,48],
            'G2': [1,2,3,4,5,6,25,26,27,10,11,12,13,14,15,34,35,36,19,20,21,22,23,24,7,8,9,28,29,30,31,32,33,16,17,18,37,38,39,40,41,42,43,44,45,54,53,52,51,50,49,48,47,46],
            'G3': [1,2,3,4,5,6,16,17,18,10,11,12,13,14,15,25,26,27,19,20,21,22,23,24,34,35,36,28,29,30,31,32,33,7,8,9,37,38,39,40,41,42,43,44,45,48,51,54,47,50,53,46,49,52],
            'PHOTO' : [1,2,3,8,0,4,7,6,5,9,10,11,16,0,12,15,14,13,41,42,43,48,0,44,47,46,45,33,34,35,40,0,36,39,38,37,29,30,31,28,0,32,27,26,25,19,20,21,18,0,22,17,24,23],

            'R1O1' : [39,2,46,38,5,47,37,8,48,16,13,10,17,14,11,18,15,12,43,20,54,44,23,53,45,26,52,34,31,28,35,32,29,36,33,30,21,24,27,40,41,42,9,6,3,25,22,19,49,50,51,1,4,7],
            'R2O2' : [27,2,25,24,5,22,21,8,19,18,17,16,15,14,13,12,11,10,9,20,7,6,23,4,3,26,1,36,35,34,33,32,31,30,29,28,54,53,52,40,41,42,48,47,46,45,44,43,49,50,51,39,38,37],
            'R3O3' : [52,2,45,53,5,44,54,8,43,12,15,18,11,14,17,10,13,16,48,20,37,47,23,38,46,26,39,30,33,36,29,32,35,28,31,34,7,4,1,40,41,42,19,22,25,3,6,9,49,50,51,27,24,21],
            'W1Y1' : [7,4,1,8,5,2,9,6,3,37,11,48,40,14,51,43,17,54,25,22,19,26,23,20,27,24,21,45,29,52,42,32,49,39,35,46,36,38,12,33,41,15,30,44,18,10,47,34,13,50,31,16,53,28],
            'W2Y2' : [9,8,7,6,5,4,3,2,1,36,11,34,33,14,31,30,17,28,27,26,25,24,23,22,21,20,19,18,29,16,15,32,13,12,35,10,46,38,48,49,41,51,52,44,54,37,47,39,40,50,42,43,53,45],
            'W3Y3' : [3,6,9,2,5,8,1,4,7,46,11,39,49,14,42,52,17,45,21,24,27,20,23,26,19,22,25,54,29,43,51,32,40,48,35,37,10,38,34,13,41,31,16,44,28,36,47,12,33,50,15,30,53,18],
            'B1G1' : [10,11,12,4,5,6,34,35,36,19,20,21,13,14,15,7,8,9,28,29,30,22,23,24,16,17,18,1,2,3,31,32,33,25,26,27,43,40,37,44,41,38,45,42,39,52,49,46,53,50,47,54,51,48],
            'B2G2' : [19,20,21,4,5,6,25,26,27,28,29,30,13,14,15,34,35,36,1,2,3,22,23,24,7,8,9,10,11,12,31,32,33,16,17,18,45,44,43,42,41,40,39,38,37,54,53,52,51,50,49,48,47,46],
            'B3G3' : [28,29,30,4,5,6,16,17,18,1,2,3,13,14,15,25,26,27,10,11,12,22,23,24,34,35,36,19,20,21,31,32,33,7,8,9,39,42,45,38,41,44,37,40,43,48,51,54,47,50,53,46,49,52]

        }[t]


Cube()