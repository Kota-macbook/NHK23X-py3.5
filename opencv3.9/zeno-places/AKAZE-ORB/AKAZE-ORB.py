import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import copy

img_C = cv2.imread("./bushitu.png")
img_G = cv2.cvtColor(img_C, cv2.COLOR_BGR2GRAY)

img_akaze = copy.deepcopy(img_C)


akaze = cv2.AKAZE_create()

kp1 = akaze.detect(img_akaze)

img_akaze = cv2.drawKeypoints(img_akaze, kp1, None)


img_orb = copy.deepcopy(img_C)

orb = cv2.ORB_create()

kp2 = orb.detect(img_orb)

img_orb = cv2.drawKeypoints(img_orb, kp2, None)

cv2.imwrite("./zeno-places/AKAZE-ORB/akaze.png",img_akaze)

cv2.imwrite("./zeno-places/AKAZE-ORB/orb.png", img_orb)
