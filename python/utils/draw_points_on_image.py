from PIL import Image, ImageDraw
import time

def draw_elipse(draw, x, y, color = (255, 0, 0), radius = 5, width = 3):
    """This function draw an ellipse on given image. 
    Params:
    - draw: Object with given image (ImageDraw.Draw(im));
    - x: x coordinate of ellipse
    - y: y coordinate of ellipse"""

    x0 = x - radius
    y0 = y - radius
    x1 = x + radius
    y1 = y + radius
    draw.ellipse([(x0, y0),(x1, y1)], None, color, width)


def draw_points_on_image(coords, image, cube_transformation, photo_transformation, up_or_down):

    array_shift = 0
    if up_or_down == 'down':
        array_shift = 0
    else:
        array_shift = 24


    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    n = 0
    for i in range(0, len(coords), 2):
        draw_elipse(draw, coords[i], coords[i+1])
        n+=1
        draw.text((coords[i]+6, coords[i+1]-6), (str(cube_transformation[photo_transformation.index(array_shift+n)])), fill="black")
        
    time.sleep(0.05)
    im.save(image)
    im.close()


