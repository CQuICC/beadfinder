import matplotlib.pyplot as plt
import numpy as np

def getBrightest(s, img, limited=False):
  r = min(round(img.shape[0] / 2), round(img.shape[1] / 2))

  s = 3
  max_img = 0
  mdp = (0, 0)
  for i in range(img.shape[0] - s):
    for j in range(img.shape[1] - s):
      if (i-r)**2 + (j-r)**2 > (r-s-1)**2 and limited:
        continue
      if np.median(img[i:i+s, j:j+s]) > max_img:
        max_img = np.median(img[i:i+s, j:j+s])

        max_x = round(np.argmax(img[i:i+s, j:j+s]) / s)
        max_y = np.argmax(img[i:i+s, j:j+s]) % s
        mdp = (i + max_x, j + max_y)

  return mdp

def plotAB(A, B, A_cap, B_cap):
  fig, axs = plt.subplots(1, 2)
  axs[0].imshow(A, cmap='gray')
  axs[0].set_title(A_cap)
  axs[1].imshow(B, cmap='gray')
  axs[1].set_title(B_cap)


roll = lambda A, i: np.roll(A, i)

def getOffset(A, B):
  if len(A) < len(B):
    A = np.pad(A, (0, len(B) - len(A)))
  else:
    B = np.pad(B, (0, len(A) - len(B)))

  offset = 0
  diffs = []
  for i in range(0, len(A)):
    diff = np.sum(np.abs(A - roll(B, i)))
    diffs.append(diff)

  offset = np.argmin(diffs)
  return offset % len(A)

def trim(imgA, imgB):
  min_x = min(imgA.shape[0], imgB.shape[0])
  min_y = min(imgA.shape[1], imgB.shape[1])

  return imgA[:min_x, :min_y], imgB[:min_x, :min_y]