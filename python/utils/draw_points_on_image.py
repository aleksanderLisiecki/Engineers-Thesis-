from PIL import Image, ImageDraw
import points as read

PATH = '/home/alex/inzynierka/'


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

coords_down = []
coords_up = []

[coords_down, coords_up] = read.read_points_from_file(PATH + 'data/points.txt')



im = Image.open('/home/alex/inzynierka/img/kostka_dol.png')
draw = ImageDraw.Draw(im)

n = 0
m = 0
for i in range(0, len(coords_down), 2):
    draw_elipse(draw, coords_down[i], coords_down[i+1])
    n+=1
    m+=1
    draw.text((coords_down[i]+6, coords_down[i+1]-6), (str(n)+'('+str(m)+')'), fill="black")
    if n==8: n=0

im.save('cube_marked_down.png')
im.close()

im = Image.open('/home/alex/inzynierka/img/kostka_gora.png')
draw = ImageDraw.Draw(im)

# m = 0
for i in range(0, len(coords_up), 2):
    draw_elipse(draw, coords_up[i], coords_up[i+1])
    n+=1
    m+=1
    draw.text((coords_up[i]+6, coords_up[i+1]-6), (str(n)+'('+str(m)+')'), fill="black")
    if n==8: n=0

im.save('cube_marked_up.png')
im.close()

