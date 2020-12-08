import kociemba
import serial

NORMAL = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
SOLVER = [37,38,39,40,41,42,43,44,45,19,20,21,22,23,24,25,26,27,10,11,12,13,14,15,16,17,18,46,47,48,49,50,51,52,53,54,1,2,3,4,5,6,7,8,9,28,29,30,31,32,33,34,35,36]


def switch(x):
  return{
    'w': 'L',
    'r': 'F',
    'y': 'R',
    'o': 'B',
    'b': 'U',
    'g': 'D'
  }[x]





kociemba_cube = "ywbrwgyrbooyyrgobgbrboywwywwgoboggbrgwrrbywwryyrbgogoo"
cube = ""

for c in kociemba_cube:
  cube += switch(c)

solver_cube_arr = [0]*54

for i in range(54):
  solver_cube_arr[NORMAL[i]-1] = cube[SOLVER[i]-1]

solver_cube = ""

for color in solver_cube_arr:
  solver_cube += color


result = kociemba.solve(solver_cube)

print(result)

alg = ">"

for move in result:
  alg += str(move);

ser = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=20)
ser.write(alg.encode())