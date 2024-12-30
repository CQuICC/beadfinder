from json import load, dump
from sys import argv

# ask user for dir
in_d = argv[1]
out_d = argv[2]
# if no dir is given, exit
if not in_d or not out_d:
  print("No directory given!")
  print("Usage: python extract.py <dir_in> <dir_out>")
  exit()

with open('data.txt', 'r') as f:
  data = load(f)
Y_AXIS = int(data['Y'])

# check if output directory exists
try:
  open(f'./{out_d}/0.png', 'w').close()
except:
  print("Creating output directory...")
  from os import mkdir as M
  M(f'./{out_d}')

from os import listdir as L
import numpy as np
import cv2 as C

# BOX position and size
B_POS = (Y_AXIS, 710)
B_SIZ = 25

# read how many images are in the directory
im_ct = len([f for f in L(f'./{in_d}') if f.endswith('.png')])

for i in range(1, im_ct):
  img = C.imread(f'./{in_d}/{i:03d}.png', C.IMREAD_GRAYSCALE)
  img = img[B_POS[0]-B_SIZ:B_POS[0]+B_SIZ, B_POS[1]-B_SIZ:B_POS[1]+B_SIZ]
  img[img < 172] = 0

  C.imwrite(f'./{out_d}/{i:03d}.png', img)

# finding the beat frequecy by checking how long it takes
# for the image to become same as the first image

B_POS = (Y_AXIS, 500)

x0, y0 = B_POS[0]-B_SIZ, B_POS[1]-B_SIZ
x1, y1 = B_POS[0]+B_SIZ, B_POS[1]+B_SIZ

OFFSET = 5
BASE = C.imread(f'./in_dir/001.png', C.IMREAD_GRAYSCALE)
BASE = BASE[x0:x1, y0:y1]

diffs = []
for i in range(OFFSET, min(100, im_ct)):
  # read image
  IMG = C.imread(f'./in_dir/{i:03d}.png', C.IMREAD_GRAYSCALE)
  box_img = IMG[x0:x1, y0:y1]

  # get difference between box and image
  diff = C.absdiff(BASE, box_img)
  diff = np.sum(diff)/(B_SIZ*2)**2

  diffs.append(diff)

# argmin of diffs
fft = np.fft.fft(diffs).astype(np.complex64)
fft = np.round(np.abs(fft), 2)
fft[0] = 0
period = round(len(diffs) / np.argmax(fft))
print(f"Beat frequency: {period} frames")

with open(f'./data.txt', 'w') as f:
  data['f'] = str(period)
  data['ct'] = str(im_ct)
  dump(data, f)