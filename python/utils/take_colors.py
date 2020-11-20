from PIL import Image, ImageDraw

def take_colors(coords, image_path):
    try:
        im = Image.open(image_path)
    except FileNotFoundError:
        print("File cube_xxx_" + image_path + " not found")
        return
    colors = []
    for i in range(0, len(coords), 2):
        pix = im.getpixel((coords[i], coords[i+1]))
        colors.append(pix)
    im.close()
    return colors