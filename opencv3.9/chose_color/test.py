import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([10,50,50])
upper = np.array([50,150,150])

frame_mask = cv2.inRange(hsv, lower, upper)

dst = cv2.bitwise_and(img, img, mask = frame_mask)



cv2.imwrite("chose_color/test.png",hsv)