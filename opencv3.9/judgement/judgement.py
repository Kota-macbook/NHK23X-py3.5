import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

threshold = 100

img = cv2.imread("./bushitu.png",0)

ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

cv2.imwrite("judgement.png",img_th)