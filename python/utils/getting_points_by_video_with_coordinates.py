import cv2

f = open('/home/pi/inzynierka/data/points.txt', 'r')

X_coords = []
Y_coords = []
i = 0
for line in f:
    if i > 1 and i < 26:
        point = line.split()
        X_coords.append(int(point[0]))
        Y_coords.append(int(point[1]))
    i += 1
    
f.close()


cv2.namedWindow("preview")
vc = cv2.VideoCapture("/dev/video2")


center_coords = (166, 204)
radius = 4
color = (255, 0 ,0) #BGR
thickness = 2



if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    for i in range(len(X_coords)):
        center_coords = (X_coords[i], Y_coords[i])
        circle = cv2.circle(frame, center_coords, radius, color,thickness)
        cv2.imshow("preview", circle)


    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")