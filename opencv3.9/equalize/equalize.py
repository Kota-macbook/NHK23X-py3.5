import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

img_eq = cv2.equalizeHist(img)

cv2.imwrite("equalized.png",img_eq)