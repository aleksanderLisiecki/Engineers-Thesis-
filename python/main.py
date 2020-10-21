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

from read_points_from_file import read_points_from_file

coords = [coords_down, coords_up] = read_points_from_file(PATH + 'python/points.txt')


#save old photos in history
import photo_history

number_of_photos_in_history = 5 

photo_history.set_number_of_photos_in_history(number_of_photos_in_history)
photo_history.set_path(PATH)
photo_history.save_history()

#make a photo



#odczytaj wartosci i zapisz je do pliku 


#obróć ściankę 

