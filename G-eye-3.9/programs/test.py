import cv2
from cv2 import threshold
import numpy as np
import math
import def_colorfilter

img = cv2.imread("./test_images/pole.png")

senter = (23, 189, 212)
haba = (4, 61, 108)

img_filtered = def_colorfilter.colorfilter(img,senter,haba)

cv2.imwrite("./test.png", img_filtered)