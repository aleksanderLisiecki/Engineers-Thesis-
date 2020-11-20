# photo history convention:
# -cube_down_new (_up also)
# -cube_down_old_0
# -cube_down_old_1
# -cube_down_old_2
# -cube_down_old_3
# -cube_down_old_4

from PIL import Image, ImageDraw

PATH = '/home/pi/inzynierka/img/cube_photos'



def _overwrite_photo(overwritten_photo, number):
    """Naming way: 'cube_down/up_' + overwritten_photo + '.jpg'"""

    def rename_cube_photo(upOrDown):
        im = Image.open(PATH + '/cube_' + upOrDown + '_' + overwritten_photo + ('_'+str(number-1) if (number > 0) else '') + '.jpg')
        im.save(PATH + '/cube_' + upOrDown + '_old_' + str(number) + '.jpg')
        im.close()
        
    try:
        rename_cube_photo('down')
        rename_cube_photo('up')
    except FileNotFoundError:
        pass
        # print("File cube_down_" + overwritten_photo + ('_'+str(number-1) if (number > 0) else '') + ".jpg not found")

def save_history():
    number_of_photos_in_history = 10
    while number_of_photos_in_history > 0:
        _overwrite_photo('old', number_of_photos_in_history)
        number_of_photos_in_history -= 1

    _overwrite_photo('new', 0)