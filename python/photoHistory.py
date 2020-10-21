# photo history convention:
# -cube_down_new (_up also)
# -cube_down_old_0
# -cube_down_old_1
# -cube_down_old_2
# -cube_down_old_3
# -cube_down_old_4

from PIL import Image, ImageDraw

numberOfPhotoInHistory = 5

def overwritePhoto(overwrittenPhoto, number):
    """Naming way: 'cube_down/up_' + overwrittenPhoto + '.jpg'"""

    def renameCubePhoto(upOrDown):
        im = Image.open('/home/alex/inzynierka/img/cube_' + upOrDown + '_' + overwrittenPhoto + ('_'+str(number-1) if (number > 0) else '') + '.jpg')
        im.save('/home/alex/inzynierka/img/cube_' + upOrDown + '_old_' + str(number) + '.jpg')
    try:
        renameCubePhoto('down')
        renameCubePhoto('up')

        # im = Image.open('/home/alex/inzynierka/img/cube_down_' + overwrittenPhoto + '.jpg')
        # im.save('/home/alex/inzynierka/img/cube_down_old' + ('' if (numberOfOldPhoto == 0) else '_' + str(numberOfOldPhoto)) + '.jpg')
        # im = Image.open('/home/alex/inzynierka/img/cube_up_' + overwrittenPhoto + '.jpg')
        # im.save('/home/alex/inzynierka/img/cube_up_old' + ('' if (numberOfOldPhoto == 0) else '_' + str(numberOfOldPhoto)) + '.jpg')
    except FileNotFoundError:
        print("File cube_down_" + overwrittenPhoto + ('_'+str(number-1) if (number > 0) else '') + ".jpg not found")


while numberOfPhotoInHistory > 0:
    overwritePhoto('old', numberOfPhotoInHistory)
    numberOfPhotoInHistory -= 1
    
overwritePhoto('new', 0)

