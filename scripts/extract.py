from sys import argv

# ask user for dir
in_d = argv[1]
out_d = argv[2]
# if no dir is given, exit
if not in_d or not out_d:
  print("No directory given!")
  print("Usage: python extract.py <dir_in> <dir_out>")
  exit()

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
B_POS = (148, 710)
B_SIZ = 25

# read how many images are in the directory
im_ct = len([f for f in L(f'./{in_d}') if f.endswith('.png')])

for i in range(1, im_ct):
  img = C.imread(f'./{in_d}/{i:03d}.png', C.IMREAD_GRAYSCALE)
  img = img[B_POS[0]-B_SIZ:B_POS[0]+B_SIZ, B_POS[1]-B_SIZ:B_POS[1]+B_SIZ]
  img[img < 172] = 0

  C.imwrite(f'./{out_d}/{i:03d}.png', img)