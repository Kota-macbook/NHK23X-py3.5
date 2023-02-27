import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import copy

img_C = cv2.imread("./bushitu.png")
img_G = cv2.cvtColor(img_C, cv2.COLOR_BGR2GRAY)

ret, img_otsu = cv2.threshold(img_G, 0, 255, cv2.THRESH_OTSU)

cv2.imwrite("./borders/otsu.png", img_otsu)

#images はアプデでいらなくなった

contours, hierarchy = cv2.findContours(img_otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_contour = cv2.drawContours(img_C, contours, -1, (255,0,0), 1)

cv2.imwrite("./borders/borders.png", img_contour)

