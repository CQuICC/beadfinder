from ast import literal_eval as make_tuple
from itertools import groupby
from json import load
from math import ceil
import numpy as np
import cv2 as C

read = lambda path: C.imread(path, C.IMREAD_GRAYSCALE)
hough = lambda img, **kwargs: np.uint16(np.around(C.HoughCircles(
  img, method=C.HOUGH_GRADIENT, dp=1, **kwargs
)))
templ = lambda img, ref: C.minMaxLoc(C.matchTemplate(ref, img, C.TM_CCOEFF_NORMED))

def getFrame(video, index):
  cap = C.VideoCapture(video)
  frame = None

  ct = 0
  while ct <= index:
    frame = cap.read()[1]
    ct += 1

  return frame

def group(lst):
  ranges = []
  for _, g in groupby(enumerate(lst), lambda k: k[0] - k[1]):
    start = next(g)[1]
    end = list(v for _, v in g) or [start]
    ranges.append(range(start, end[-1] + 1))

  for R in range(len(ranges)):
    if R == 0 or ranges[R] is None or ranges[R - 1] is None:
      continue
    if ranges[R].start - ranges[R - 1].stop <= 2:
      ranges[R - 1] = range(ranges[R - 1].start, ranges[R].stop)
      ranges[R] = None

  return [r for r in ranges if r is not None]

def xy(B_POS, B_SIZ):
  x0, y0 = B_POS[0]-B_SIZ, B_POS[1]-B_SIZ
  x1, y1 = B_POS[0]+B_SIZ, B_POS[1]+B_SIZ

  return x0, y0, x1, y1

def Circ(img):
  CC = hough(
    img, minDist=1, param1=100, param2=15,
    minRadius=1, maxRadius=20
  )[0][0]
  x, y, r = CC[0], CC[1], (ceil(CC[2]) + 1)

  img2 = img.copy()
  img2 = 255 - img2 * C.circle(np.zeros_like(img2), (x, y), r, 255, -1)
  img2 = img2[y-r:y+r, x-r:x+r]

  return img2

def parseData():
  data = load(open('data.txt', 'r'))

  file = data['file']
  index = int(data['index'])
  sz = make_tuple(data['sz'])
  Y_AXIS = int(data['Y'])
  BEAD_FREQ = int(data['f'])
  CT = int(data['ct']) + 1
  BBOX = make_tuple(data['bsz'])

  BEAD_SIZE = float(data['R'])
  IBD = float(data['D'])

  return file, sz, Y_AXIS, BEAD_FREQ, CT, BBOX, BEAD_SIZE, IBD, index