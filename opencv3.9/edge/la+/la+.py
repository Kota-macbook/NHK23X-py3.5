import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

img_lap = cv2.Laplacian(img,cv2.CV_32F)

img_lap = cv2.convertScaleAbs(img_lap)

cv2.imwrite("./edge/la+/la+.png",img_lap)