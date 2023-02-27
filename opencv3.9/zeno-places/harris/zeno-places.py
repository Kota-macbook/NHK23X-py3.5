import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import copy

img_C = cv2.imread("./bushitu.png")
img_G = cv2.cvtColor(img_C, cv2.COLOR_BGR2GRAY)

img_harris = copy.deepcopy(img_C)

img_dst = cv2.cornerHarris(img_G, 2, 3, 0.04)

img_harris[img_dst > 0.05 * img_dst.max()] = [0, 0, 255]

img_reduct = img_harris - img_C

cv2.imwrite("./zeno-places/harris/harris.png",img_harris)

cv2.imwrite("./zeno-places/harris/reduct.png",img_reduct)