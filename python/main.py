PATH = '/home/alex/inzynierka/'


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

import read_points_from_file

coords = [coords_down, coords_up] = read_points_from_file.read_points_from_file(PATH + 'data/points.txt')


#save old photos in history
import photo_history

number_of_photos_in_history = 5 

photo_history.set_number_of_photos_in_history(number_of_photos_in_history)
photo_history.set_path(PATH)
photo_history.save_history()

#make a photo
import make_a_photo

make_a_photo.make_a_photo('/dev/video0', '/dev/video0')

#take the color values and save it



#obróć ściankę 

