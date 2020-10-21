
def read_points_from_file(file = '/home/alex/inzynierka/python/points.txt'):
    """This function gets an file with points on cube and return 2 dim array with x & y points 
    """
    f = open(file, 'r')
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
    return [coords_down, coords_up]