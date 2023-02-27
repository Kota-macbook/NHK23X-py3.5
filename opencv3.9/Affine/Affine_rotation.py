import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png")

h, w = img.shape[:2]

rot_mat = cv2.getRotationMatrix2D((w/2,h/2),30,2)

print(rot_mat)

img_rot = cv2.warpAffine(img, rot_mat, (w,h))

cv2.imwrite("afn_rotation.png",img_rot)