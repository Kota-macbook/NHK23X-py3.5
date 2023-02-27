import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./line_circle.jpg",0)

h,w = img.shape[:2]

h_50 = h/4

w_50 = w/4

h_w_large = (h_50 + w_50)/2

h_w_noise = h_w_large/2

#circles

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=1, minDist=1, param1=h_w_noise, param2=35, minRadius=100, maxRadius=250)

#print(circles.shape)

#[[[a b c],[d e f],.....]]

#print(circles[0])

for i in circles[0]:
    
    #print(str( i[0] ) + "/n" + str( i[1] ) + "¥t" + str( i[2] ))
    
    cv2.circle(img, (int(i[0]),int(i[1])), int(i[2]), (0, 255, 0), 1)
    
cv2.imwrite("./edge/circle_canny/circles.png",img)
