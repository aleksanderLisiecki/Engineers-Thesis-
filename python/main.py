import cube
from utils import history
from utils import make_a_photo

PATH = '/home/alex/inzynierka/'

#save old photos in history
number_of_photos_in_history = 5 

history.set_number_of_photos_in_history(number_of_photos_in_history)
history.set_path(PATH)
history.save_history()

#make a photo
# make_a_photo.make_a_photo('/dev/video0', '/dev/video0')



cube = cube.Cube()

#take the color values and save it 

# cube.take_colors()

# assign colors to arrays




#turn cube wall 

