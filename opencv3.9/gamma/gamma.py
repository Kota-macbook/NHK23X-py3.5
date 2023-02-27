import cv2
import numpy as np
import matplotlib as mp

img = cv2.imread("./IMG_6071.JPG")

gamma = 1.8

gamma_cvt = np.zeros((256,1),dtype=np.uint8)

for i in range(256):
    
    gamma_cvt[i][0] = 255 * (float(i) / 255) ** (1.0 / gamma)

img_gamma = cv2.LUT(img,gamma_cvt)

cv2.imwrite("gamma.png",img_gamma)