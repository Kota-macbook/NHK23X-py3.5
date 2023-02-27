import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png")
img_G = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

