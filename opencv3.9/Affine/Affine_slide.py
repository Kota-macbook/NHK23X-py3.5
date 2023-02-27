import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png")

h, w = img.shape[:2]

dx, dy = 50, 50

afn_mat = np.float32([[1,0,dx],[0,1,dy]])

img_afn = cv2.warpAffine(img, afn_mat, (w,h))

cv2.imwrite("afn_slide.png",img_afn)