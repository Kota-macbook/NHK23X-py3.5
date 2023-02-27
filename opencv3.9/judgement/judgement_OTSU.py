import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

ret, img_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

cv2.imwrite("judgement_OTSU.png",img_otsu)