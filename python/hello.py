
red_wall = [9]
yellow_wall = [9]
orange_wall = [9]
white_wall = [9]
blue_wall = [9]
green_wall = [9]


#get an coords of points

coords = [[],[]]
coords_down = []
coords_up = []

from read_points_from_file import read_points_from_file

coords = [coords_down, coords_up] = read_points_from_file('/home/alex/inzynierka/python/points.txt')


#put old photos in hitory ()
from PIL import Image, ImageDraw

number_of_photo_in_history = 5

def overwrite_photo():
    im = Image.open('/home/alex/inzynierka/img/cube_down_new.jpg')
    im.save('img/cube_down_old' + str(number_of_photo_in_history) + '.jpg')

for number in range(number_of_photo_in_history-1):
    im = Image.open('/home/alex/inzynierka/img/cube_old' + ('' if 0 else str(number + 1)) + '.jpg')
    im.save('img/cube_old' + str(number_of_photo_in_history) + '.jpg')
#END - photo's history


#make a photo  

#photo's history
from PIL import Image, ImageDraw

number_of_photo_in_history = 5

def overwrite_photo():
    im = Image.open('/home/alex/inzynierka/img/cube_down_new.jpg')
    im.save('img/cube_down_old' + str(number_of_photo_in_history) + '.jpg')

for number in range(number_of_photo_in_history-1):
    im = Image.open('/home/alex/inzynierka/img/cube_old' + ('' if 0 else str(number + 1)) + '.jpg')
    im.save('img/cube_old' + str(number_of_photo_in_history) + '.jpg')
#END - photo's history


#odczytaj wartosci i zapisz je do pliku 


#obróć ściankę 


