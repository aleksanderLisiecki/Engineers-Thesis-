
from rubik_solver import utils
import sys
import yaml
import time
import serial

NORMAL = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
SOLVER = [21,24,27,20,23,26,19,22,25,39,42,45,38,41,44,37,40,43,12,15,18,11,14,17,10,13,16,48,51,54,47,50,53,46,49,52,30,33,36,29,32,35,28,31,34,3,6,9,2,5,8,1,4,7]

def yaml_loader(filepath):
  with open(filepath, "r") as f:
    data = yaml.load(f, Loader= yaml.Loader)
  last_key_number = 0
  for key in data.keys():
    last_key_number = key
  return data, last_key_number

filepath = ""
try:
  filepath = sys.argv[1]
except:
  print("Podaj ścieżkę pliku yaml z danymi terningowymi")
  sys.exit()

data, last_key = yaml_loader(filepath)

colors = data[last_key]['colors']

cube = ""
for color in colors:
  cube += str(color)

# cube = "bgyowrwbobyyyrgbggggbwyooyrybrwobyrgwroyborbowrwwgorwg"


print(cube)

solver_cube_arr = [0]*54

for i in range(54):
  solver_cube_arr[NORMAL[i]-1] = cube[SOLVER[i]-1]


solver_cube = ""

for color in solver_cube_arr:
  solver_cube += color

print("Zaczynam obliczanie algorytmu")
start = time.time()

result = utils.solve(solver_cube, 'Kociemba')

end = time.time()
print("time: " + str(end - start))

print(result)

alg = ""

for move in result:
  alg += str(move);

print(alg)

# # ser = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=20)
# # ser.write(alg.encode())

# end = time.time()
# print("time: " + str(end - start))
 