import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

ret, img_th = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

kernel = np.ones((3,3),dtype=np.uint8)

img_c = cv2.morphologyEx(img_th, cv2.MORPH_CLOSE, kernel)

img_d = cv2.dilate(img_th, kernel)

cv2.imwrite("./morphology/closing/closing.png", img_c)

cv2.imwrite("./morphology/closing/dilate.png", img_d)