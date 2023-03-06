import cv2
import numpy as np


size = (5,5,3)
img = np.zeros(size,dtype=np.uint16)

for i in range(size[0]):
    for j in range(size[1]):
        for k in range(size[2]):
            img[i][j][k]=i + j + k

print(img)

img2 = img < 5

print(img2)

img3 = np.all(img < 5)

print(img3)