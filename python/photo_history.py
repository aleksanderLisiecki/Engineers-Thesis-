# photo history convention:
# -cube_down_new (_up also)
# -cube_down_old_0
# -cube_down_old_1
# -cube_down_old_2
# -cube_down_old_3
# -cube_down_old_4

from PIL import Image, ImageDraw

path = '/home/alex/inzynierka/'

number_of_photos_in_history = 5

def set_number_of_photos_in_history(number):
    global number_of_photos_in_history
    number_of_photos_in_history = number

def set_path(p):
    global path
    path = p

def overwrite_photo(overwritten_photo, number):
    """Naming way: 'cube_down/up_' + overwritten_photo + '.jpg'"""

    def rename_cube_photo(upOrDown):
        im = Image.open(path + 'img/cube_' + upOrDown + '_' + overwritten_photo + ('_'+str(number-1) if (number > 0) else '') + '.jpg')
        im.save(path + 'img/cube_' + upOrDown + '_old_' + str(number) + '.jpg')
    try:
        rename_cube_photo('down')
        rename_cube_photo('up')
    except FileNotFoundError:
        print("File cube_down_" + overwritten_photo + ('_'+str(number-1) if (number > 0) else '') + ".jpg not found")

def save_history():
    global number_of_photos_in_history
    while number_of_photos_in_history > 0:
        overwrite_photo('old', number_of_photos_in_history)
        number_of_photos_in_history -= 1

    overwrite_photo('new', 0)