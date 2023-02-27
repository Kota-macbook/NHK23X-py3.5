import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import copy

img_C = cv2.imread("./blob/pole.png")
img_G = cv2.cvtColor(img_C, cv2.COLOR_BGR2GRAY)

ret, img_otsu = cv2.threshold(img_G, 0, 255, cv2.THRESH_OTSU)

cv2.imwrite("./blob/otsu.png", img_otsu)

nLabels, labelImages, stats, centroids = cv2.connectedComponentsWithStats(img_otsu)

print(labelImages.shape)

img_blob = copy.deepcopy(img_C)

h, w = img_G.shape[:2]

colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [0, 255, 255], [255, 0, 255], [255, 255, 255]]

for y in range(h):
    for x in range(w):
        if labelImages[y, x] >0:
            c_const = labelImages[y,x] - 1
            #print(c_const)
            img_blob[y,x] = colors[labelImages[y, x] % 7]

for i in range(1, nLabels):
    xc = int(centroids[i][0])
    yc = int(centroids[i][1])
    
    font = cv2.FONT_HERSHEY_COMPLEX
    scale = 1
    color = (255, 0,0)
    
    cv2.putText(img_blob, str(stats[i][-1]), (xc,yc), font, scale, color)
    
    
cv2.imwrite("./blob/blob.png",img_blob)