import cv2
import numpy as np

img_color = cv2.imread("./parametor1/export.png")

img = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

h,w = img.shape[:2]

darkness = [255,255,255]

whiteness = [0,0,0]

for i in range(h):
    for j in range(w):
        for k in range(3):
            if darkness[k]>img[i][j][k]:
                darkness[k]=img[i][j][k]
            if whiteness[k]<img[i][j][k]:
                whiteness[k]=img[i][j][k]

print("darkness="+str(darkness))
print("whiteness="+str(whiteness))

#darkness=[21, 128, 103]
#whiteness=[24, 221, 255]