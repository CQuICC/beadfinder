from itertools import groupby
from os import listdir as L
import numpy as np
import cv2 as C

def to_ranges(lst):
  ranges = []
  for _, g in groupby(enumerate(lst), lambda k: k[0] - k[1]):
    start = next(g)[1]
    end = list(v for _, v in g) or [start]
    ranges.append(range(start, end[-1] + 1))

  return ranges

def count_im(dir):
  ct = [f for f in L(dir) if f.endswith('.png')]
  if '0.png' in ct:
    ct.remove('0.png')
  if '000.png' in ct:
    ct.remove('000.png')

  return len(ct)

def xy(B_POS, B_SIZ):
  x0, y0 = B_POS[0]-B_SIZ, B_POS[1]-B_SIZ
  x1, y1 = B_POS[0]+B_SIZ, B_POS[1]+B_SIZ

  return x0, y0, x1, y1

def Circ(img, R):
  rme, rpe = round(R * 0.9), round(R * 1.1)

  detected = np.uint16(np.around(C.HoughCircles(
    img, method=C.HOUGH_GRADIENT, dp=1,
    minDist=1, param1=100, param2=10,
    minRadius=rme, maxRadius=rpe
  )))[0][0]

  x, y, r = detected
  r=r+1

  img2 = img.copy()
  img2 = 255 - img2 * C.circle(np.zeros_like(img2), (x, y), r, 255, -1)
  img2 = img2[y-r:y+r, x-r:x+r]

  return img2