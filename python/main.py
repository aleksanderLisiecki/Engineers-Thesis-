import read_points_from_file
import history
import make_a_photo
import colors

PATH = '/home/alex/inzynierka/'

#save old photos in history
number_of_photos_in_history = 5 

history.set_number_of_photos_in_history(number_of_photos_in_history)
history.set_path(PATH)
history.save_history()

#make a photo
# make_a_photo.make_a_photo('/dev/video0', '/dev/video0')

#get an coords of points
red_wall = [9]
yellow_wall = [9]
orange_wall = [9]
white_wall = [9]
blue_wall = [9]
green_wall = [9]
cube = [red_wall, yellow_wall, orange_wall, white_wall, blue_wall, green_wall]

coords = [[],[]]
coords_down = []
coords_up = []

cube_colors = [[],[]]
cube_colors_down = []
cube_colors_up = []

coords = [coords_down, coords_up] = read_points_from_file.read_points_from_file(PATH + 'data/points.txt')

#take the color values and save it 

cube_colors_down = colors.take_colors(coords_down, PATH+'img/cube_down_new.jpg')
cube_colors_up = colors.take_colors(coords_up, PATH+'img/cube_up_new.jpg')


#obróć ściankę 

