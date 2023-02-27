import cv2
from cv2 import threshold
import numpy as np
import math
#自作関数、場所は./programs/def_colorfilter.py
import def_colorfilter
import blob

#import the images
img = cv2.imread("./test_images/pole.png")

img_colorfiltered = def_colorfilter.colorfilter(img,(23,189,212),(4, 61, 108))

img_Gray = cv2.cvtColor(img_colorfiltered, cv2.COLOR_BGR2GRAY)
cv2.imwrite("./filtered_images/1_img.png", img)
cv2.imwrite("./filtered_images/2_img_Gray.png", img_Gray)

#get high weigh
h,w = img_Gray.shape[:2]
h_2 = h/5
w_2 = w/5

#contrast up
#img_eq = cv2.equalizeHist(img_Gray)
#cv2.imwrite("./filtered_images/3_img_eq.png", img_eq)

#kill noises
img_bi = cv2.bilateralFilter(img_Gray, 30, 30, 200)
cv2.imwrite("./filtered_images/4_img_bi.png", img_bi)

#judgement-ada
h_w = h+w
size_ada = int(h_w / 135)
#size_adaは奇数じゃないとimg_ada(5行下)がエラーになる
#if size_ada%2 == 0:
#    size_ada += 1
#img_ada = cv2.adaptiveThreshold(img_bi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, size_ada, -5)
#cv2.imwrite("./filtered_images/5_img_ada.png", img_ada)

#judgement-otsu
ret, img_otsu = cv2.threshold(img_bi, 0, 255, cv2.THRESH_OTSU)
cv2.imwrite("./filtered_images/5_img_Otsu.png", img_otsu)

#closing
kernel = np.ones((5,5), dtype = np.uint8)
img_close = cv2.morphologyEx(img_otsu, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("./filtered_images/6_img_close.png", img_close)

#edge
h_w_large = (h_2 + w_2)/2
h_w_noise = h_w_large*(0.8)
img_canny = cv2.Canny(img_close,h_w_noise,h_w_large)
cv2.imwrite("./filtered_images/7_img_canny.png", img_canny)

#輪郭検出

contours, hierarchy = cv2.findContours(img_otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_contour = cv2.drawContours(img, contours, -1, (255,0,0), 1)

cv2.imwrite("./filtered_images/8_img_contours.png", img_contour)

#塊検出

#img_blob = blob.(img, img_otsu)

#cv2.imwrite("./filtered_images/9_img_blob.png", img_blob)