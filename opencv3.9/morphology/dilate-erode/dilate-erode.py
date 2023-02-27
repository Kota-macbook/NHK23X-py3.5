import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

ret, img_th = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

kernel = np.ones((4,4),dtype=np.uint8)

img_d = cv2.dilate(img_th, kernel)

img_e = cv2.erode(img_th, kernel)

cv2.imwrite("./morphology/dilate-erode/dilate.png", img_d)

cv2.imwrite("./morphology/dilate-erode/erode.png", img_e)