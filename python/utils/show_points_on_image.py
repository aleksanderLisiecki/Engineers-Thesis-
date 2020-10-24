import cv2

f = open('/home/alex/inzynierka/data/points.txt', 'r')

coords_down = []
coords_up = []
i = 0
for line in f:
    point = line.split()
    if i > 1 and i < 26:
        coords_down.append(int(point[0]))
        coords_down.append(int(point[1]))
    elif i > 28 and i < 53:
        coords_up.append(int(point[0]))
        coords_up.append(int(point[1]))
    i += 1
    
f.close()

center_coords = (166, 204)
radius = 4
color = (255, 0 ,0) #BGR
thickness = 2


img = cv2.imread('/home/alex/inzynierka/img/kostka_dol.png')

cv2.imshow('image', img)
for i in range(0, len(coords_down), 2):
        center_coords = (coords_down[i], coords_down[i+1])
        circle = cv2.circle(img, center_coords, radius, color,thickness)
        cv2.imshow("image", circle)

img = cv2.imread('/home/alex/inzynierka/img/kostka_gora.png')

cv2.imshow('image2', img)
for i in range(0, len(coords_up), 2):
        center_coords = (coords_up[i], coords_up[i+1])
        circle = cv2.circle(img, center_coords, radius, color,thickness)
        cv2.imshow('image2', circle)


while 1:

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyAllWindows()  