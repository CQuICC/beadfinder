from itertools import groupby
from math import ceil
import numpy as np
import cv2 as C

read = lambda path: C.imread(path, C.IMREAD_GRAYSCALE)
hough = lambda img, **kwargs: np.uint16(np.around(C.HoughCircles(
  img, method=C.HOUGH_GRADIENT, dp=1, **kwargs
)))

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

  return ranges

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