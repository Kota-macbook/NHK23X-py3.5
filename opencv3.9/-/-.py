import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png")

img_2 = cv2.imread("./IMG_6071.JPG")

img_out = img - img_2

cv2.imwrite("-.png",img_out)