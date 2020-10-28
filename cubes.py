# NORMAL
#           |37 38 39|
#           |40 b  42|
#           |43 44 45|
# | 1  2  3 |10 11 12|19 20 21|28 29 30|
# | 4  w  6 |13 r  15|22 y  24|31 o  33|
# | 7  8  9 |16 17 18|25 26 27|34 35 36|
#           |46 47 48|
#           |49 g  51|
#           |52 53 54|


normal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]

points_on_photos = [1,2,3,8,0,4,7,6,5,9,10,11,16,0,12,15,14,13,41,42,43,48,0,44,47,46,45,33,34,35,40,0,36,39,38,37,29,30,31,28,0,32,27,26,25,19,20,21,18,0,22,17,24,23]

# RED WALL 90deg (red wall rotate by 90deg clockwise)
R1 = [1,2,46,4,5,47,7,8,48,16,13,10,17,14,11,18,15,12,43,20,21,44,23,24,45,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,9,6,3,25,22,19,49,50,51,52,53,54]

# RED WALL 180deg (red wall rotate by 180deg)
R2 = [1,2,25,4,5,22,7,8,19,18,17,16,15,14,13,12,11,10,9,20,21,6,23,24,3,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,48,47,46,45,44,43,49,50,51,52,53,54]

# RED WALL 270deg (red wall rotate by 90deg counterclockwise)
R3 = [1,2,45,4,5,44,7,8,43,12,15,18,11,14,17,10,13,16,48,20,21,47,23,24,46,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,19,22,25,3,6,9,49,50,51,52,53,54]


# WHITE WALL 90deg (white wall rotate by 90deg clockwise)
W1 = [7,4,1,8,5,2,9,6,3,37,11,12,40,14,15,43,17,18,19,20,21,22,23,24,25,26,27,28,29,52,31,32,49,34,35,46,36,38,39,33,41,42,30,44,45,10,47,48,13,50,51,16,53,54]

# WHITE WALL 180deg (white wall rotate by 180deg)
W2 = [9,8,7,6,5,4,3,2,1,36,11,12,33,14,15,30,17,18,19,20,21,22,23,24,25,26,27,28,29,16,31,32,13,34,35,10,46,38,39,49,41,42,52,44,45,37,47,48,40,50,51,43,53,54]

# WHITE WALL 270deg (white wall rotate by 90deg counterclockwise)
W3 = [3,6,9,2,5,8,1,4,7,46,11,12,49,14,15,52,17,18,19,20,21,22,23,24,25,26,27,28,29,43,31,32,40,34,35,37,10,38,39,13,41,42,16,44,45,36,47,48,33,50,51,30,53,54]


# YELLOW WALL 90deg (yellow wall rotate by 90deg clockwise)
Y1 = [1,2,3,4,5,6,7,8,9,10,11,48,13,14,51,16,17,54,25,22,19,26,23,20,27,24,21,45,29,30,42,32,33,39,35,36,37,38,12,40,41,15,43,44,18,46,47,34,49,50,31,52,53,28]

# YELLOW WALL 180deg (yellow wall rotate by 180deg)
Y2 = [1,2,3,4,5,6,7,8,9,10,11,34,13,14,31,16,17,28,27,26,25,24,23,22,21,20,19,18,29,30,15,32,33,12,35,36,37,38,48,40,41,51,43,44,54,46,47,39,49,50,42,52,53,45]

# YELLOW WALL 270deg (yellow wall rotate by 90deg counterclockwise)
Y3 = [1,2,3,4,5,6,7,8,9,10,11,39,13,14,42,16,17,45,21,24,27,20,23,26,19,22,25,54,29,30,51,32,33,48,35,36,37,38,34,40,41,31,43,44,28,46,47,12,49,50,15,52,53,18]


# ORANGE WALL 90deg (orange wall rotate by 90deg clockwise)
O1 = [39,2,3,38,5,6,37,8,9,10,11,12,13,14,15,16,17,18,19,20,54,22,23,53,25,26,52,34,31,28,35,32,29,36,33,30,21,24,27,40,41,42,43,44,45,46,47,48,49,50,51,1,4,7]

# ORANGE WALL 180deg (orange wall rotate by 180deg)
O2 = [27,2,3,24,5,6,21,8,9,10,11,12,13,14,15,16,17,18,19,20,7,22,23,4,25,26,1,36,35,34,33,32,31,30,29,28,54,53,52,40,41,42,43,44,45,46,47,48,49,50,51,39,38,37]

# ORANGE WALL 270deg (orange wall rotate by 90deg counterclockwise)
O3 = [52,2,3,53,5,6,54,8,9,10,11,12,13,14,15,16,17,18,19,20,37,22,23,38,25,26,39,30,33,36,29,32,35,28,31,34,7,4,1,40,41,42,43,44,45,46,47,48,49,50,51,27,24,21]


# BLUE WALL 90deg (blue wall rotate by 90deg clockwise)
B1 = [10,11,12,4,5,6,7,8,9,19,20,21,13,14,15,16,17,18,54,53,52,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,43,40,37,44,41,38,45,42,39,46,47,48,49,50,51,3,2,1]

# BLUE WALL 180deg (blue wall rotate by 180deg)
B2 = [19,20,21,4,5,6,7,8,9,54,53,52,13,14,15,16,17,18,1,2,3,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,45,44,43,42,41,40,39,38,37,46,47,48,49,50,51,12,11,10]

# BLUE WALL 270deg (blue wall rotate by 90deg counterclockwise)
B3 = [54,53,52,4,5,6,7,8,9,1,2,3,13,14,15,16,17,18,10,11,12,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,42,45,38,41,44,37,40,43,46,47,48,49,50,51,21,20,19]


# GREEN WALL 90deg (green wall rotate by 90deg clockwise)
G1 = [1,2,3,4,5,6,39,38,37,10,11,12,13,14,15,7,8,9,19,20,21,22,23,24,16,17,18,28,29,30,31,32,33,34,35,36,27,26,25,40,41,42,43,44,45,52,49,46,53,50,47,54,51,48]

# GREEN WALL 180deg (green wall rotate by 180deg)
G2 = [1,2,3,4,5,6,25,26,27,10,11,12,13,14,15,39,38,37,19,20,21,22,23,24,7,8,9,28,29,30,31,32,33,34,35,36,18,17,16,40,41,42,43,44,45,54,53,52,51,50,49,48,47,46]

# GREEN WALL 180deg (green wall rotate by 90deg counterclockwise)
G3 = [1,2,3,4,5,6,16,17,18,10,11,12,13,14,15,25,26,27,19,20,21,22,23,24,39,38,37,28,29,30,31,32,33,34,35,36,9,8,7,40,41,42,43,44,45,48,51,54,47,50,53,46,49,52]



# lists_to_sort = [R1, R2, R3, W1, W2, W3, Y1, Y2, Y3, O1, O2, O3, B1, B2, B3, G1, G2, G3]

# print("I'm starting checking the lists!")
# errors = False
# for x in lists_to_sort:
#   y = sorted(x)

#   for i in range(len(y)):
#     if y[i] != i+1:
#       errors = True
#       print(y[i])
#       print(x)

#     # print christmas tree for checking
#     # for n in range(i):
#     #   print('*', end = '')
#     # print('')
# print("There is no missing numbers :)") if not errors else print("There was something wrong! :o")

# merge 2 moves 
def merge_moves(move1, move2):
    merged = [0] * 54
    for i in range(54):
        if move1[i] != i+1:
            merged[i] = move1[i]
        elif move2[i] != i+1:
            merged[i] = move2[i]
        else:
            merged[i] = i+1
    return merged

print(merge_moves(B1, G1))



R1O1 = [39,2,46,38,5,47,37,8,48,16,13,10,17,14,11,18,15,12,43,20,54,44,23,53,45,26,52,34,31,28,35,32,29,36,33,30,21,24,27,40,41,42,9,6,3,25,22,19,49,50,51,1,4,7]
R2O2 = [27,2,25,24,5,22,21,8,19,18,17,16,15,14,13,12,11,10,9,20,7,6,23,4,3,26,1,36,35,34,33,32,31,30,29,28,54,53,52,40,41,42,48,47,46,45,44,43,49,50,51,39,38,37]
R3O3 = [52,2,45,53,5,44,54,8,43,12,15,18,11,14,17,10,13,16,48,20,37,47,23,38,46,26,39,30,33,36,29,32,35,28,31,34,7,4,1,40,41,42,19,22,25,3,6,9,49,50,51,27,24,21]
W1Y1 = [7,4,1,8,5,2,9,6,3,37,11,48,40,14,51,43,17,54,25,22,19,26,23,20,27,24,21,45,29,52,42,32,49,39,35,46,36,38,12,33,41,15,30,44,18,10,47,34,13,50,31,16,53,28]
W2Y2 = [9,8,7,6,5,4,3,2,1,36,11,34,33,14,31,30,17,28,27,26,25,24,23,22,21,20,19,18,29,16,15,32,13,12,35,10,46,38,48,49,41,51,52,44,54,37,47,39,40,50,42,43,53,45]
W3Y3 = [3,6,9,2,5,8,1,4,7,46,11,39,49,14,42,52,17,45,21,24,27,20,23,26,19,22,25,54,29,43,51,32,40,48,35,37,10,38,34,13,41,31,16,44,28,36,47,12,33,50,15,30,53,18]
B1G1 = [10,11,12,4,5,6,39,38,37,19,20,21,13,14,15,7,8,9,54,53,52,22,23,24,16,17,18,28,29,30,31,32,33,34,35,36,43,40,37,44,41,38,45,42,39,52,49,46,53,50,47,3,2,1]
B2G2 = [19,20,21,4,5,6,25,26,27,54,53,52,13,14,15,39,38,37,1,2,3,22,23,24,7,8,9,28,29,30,31,32,33,34,35,36,45,44,43,42,41,40,39,38,37,54,53,52,51,50,49,12,11,10]
B3G3 = [10,11,12,4,5,6,39,38,37,19,20,21,13,14,15,7,8,9,54,53,52,22,23,24,16,17,18,28,29,30,31,32,33,34,35,36,43,40,37,44,41,38,45,42,39,52,49,46,53,50,47,3,2,1]

