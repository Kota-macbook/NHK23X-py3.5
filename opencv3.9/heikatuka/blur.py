import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

img_blur = cv2.blur(img, (3,3))

cv2.imwrite("./heikatuka/blur.png",img_blur)