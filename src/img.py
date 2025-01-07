import numpy as np

def getBrightest(s, img):
  s = 3
  max_img = 0
  mdp = (0, 0)
  for i in range(img.shape[0] - s):
    for j in range(img.shape[1] - s):
      if np.median(img[i:i+s, j:j+s]) > max_img:
        max_img = np.median(img[i:i+s, j:j+s])

        max_x = round(np.argmax(img[i:i+s, j:j+s]) / s)
        max_y = np.argmax(img[i:i+s, j:j+s]) % s
        mdp = (i + max_x, j + max_y)

  return mdp