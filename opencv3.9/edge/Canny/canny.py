import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

h,w = img.shape[:2]

h_50 = h/15

w_50 = w/15

h_w_large = (h_50 + w_50)/2

h_w_noise = h_w_large/2

img_canny = cv2.Canny(img,h_w_noise,h_w_large)

cv2.imwrite("./edge/Canny/Canny.png",img_canny)