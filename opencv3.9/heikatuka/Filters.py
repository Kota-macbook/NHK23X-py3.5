import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

img_ga = cv2.GaussianBlur(img, (3,3), 2)

img_me = cv2.medianBlur(img, 5)

img_bi = cv2.bilateralFilter(img, 20,30,30)

cv2.imwrite("./heikatuka/gaussian.png", img_ga)

cv2.imwrite("./heikatuka/median.png", img_me)

cv2.imwrite("./heikatuka/bilateral.png", img_bi)