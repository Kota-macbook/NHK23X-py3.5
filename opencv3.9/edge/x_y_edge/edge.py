import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

img_sobelx = cv2.Sobel(img,cv2.CV_32F,1,0,ksize=3)

img_sobely = cv2.Sobel(img,cv2.CV_32F,0,1,ksize=3)

img_sobelx = cv2.convertScaleAbs(img_sobelx)

img_sobely = cv2.convertScaleAbs(img_sobely)

cv2.imwrite("./edge/x_y_edge/sobelx.png",img_sobelx)

cv2.imwrite("./edge/x_y_edge/sobely.png",img_sobely)