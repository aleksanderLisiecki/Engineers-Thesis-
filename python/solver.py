from PIL import Image, ImageDraw
import time


def draw_cube(colors, number=''):
  """
  This function draw an flat view of given colors.
  """
  cube_draw_points_x = [0,1,2,3,4,5,6,7,8,9,10,11,3,4,5,3,4,5]
  cube_draw_points_y = [3,4,5,3,4,5,3,4,5,3,4,5,0,1,2,6,7,8]
  im = Image.new(mode = "RGB", size = (480, 360), color = (255,255,255))
  draw = ImageDraw.Draw(im)
  n = 0
  for i in range(len(cube_draw_points_y)):
      y = cube_draw_points_y[i]
      for j in range(3):
          x = cube_draw_points_x[int(i/3)*3 + j]
          draw.rectangle(((x*40,y*40),((x*40)+40,(y*40)+40)), fill=(colors[n]), outline=(0,0,0), width=2)
          # draw.text(((x*40)+16,(y*40)+16),fill=(100,100,100), text=str(self.cube_transform.index(n+1)+1))
          n+=1
  im.show(title="s")
  time.sleep(1)
  # im.save(self.PATH+'img/flat_views/flat_view'+ str(number) +'.png')
  im.close()

colors = [(12, 117, 241), (22, 28, 46), (29, 69, 90), (168, 111, 101), 0, (25, 20, 22), (23, 118, 232), (255, 224, 138), (255, 159, 86), (26, 60, 114), (13, 3, 20), (198, 198, 196), (240, 64, 51), 0, (215, 214, 203), (241, 116, 56), (33, 24, 38), (37, 33, 39), (19, 17, 17), (5, 3, 3), (12, 10, 10), (75, 73, 73), 0, (146, 131, 125), (91, 92, 83), (35, 41, 46), (66, 38, 43), (86, 29, 32), (28, 19, 31), (168, 168, 166), (34, 53, 49), 0, (30, 21, 38), (53, 52, 71), (45, 67, 69), (49, 58, 60), (187, 185, 179), (34, 64, 61), (8, 0, 12), (122, 127, 111), 0, (135, 137, 138), (112, 114, 98), (121, 123, 122), (79, 77, 62), (28, 26, 40), (47, 56, 97), (165, 172, 170), (28, 27, 34), 0, (157, 160, 156), (29, 203, 187), (255, 255, 165), (77, 71, 64)]
draw_cube(colors)