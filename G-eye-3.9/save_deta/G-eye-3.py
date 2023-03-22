import cv2
#from cv2 import threshold
#import numpy as np
#import math
#自作関数、場所は./programs/def_colorfilter.py
import def_colorfilter
import test_images.blob as blob
#import addition_img
import copy
import shirushi

#画像をインポート
img = cv2.imread("./test_images/camera3.png")
h,w = img.shape[:2]
#ポールの色を抽出
img_colorfiltered = def_colorfilter.colorfilter(img,(23,189,212),(0, 61, 108))
img_Gray = cv2.cvtColor(img_colorfiltered, cv2.COLOR_BGR2GRAY)

#ノイズキャンセル
#img_bi = cv2.bilateralFilter(img_Gray, 30, 30, 200)

#2値化
border = 103
ret, img_judged = cv2.threshold(img_Gray, border, 255, cv2.THRESH_BINARY)

#塊検出
nLabels, img_blob, stats, centroids= blob.blobs(img_judged,1000)

#番号割り振り画像作成
img_num = copy.deepcopy(img)
img_num = shirushi.shirushi(img_num,h,nLabels,stats,centroids)


#img_numbered = addition_img.addition_img(img,img_blob)
        


cv2.imwrite("./filtered_images/1_img.png", img)
cv2.imwrite("./filtered_images/2_img_color.png", img_colorfiltered)
cv2.imwrite("./filtered_images/3_img_Gray.png", img_Gray)
#cv2.imwrite("./filtered_images/4_img_bi.png", img_bi)
cv2.imwrite("./filtered_images/5_img_judged.png", img_judged)
cv2.imwrite("./filtered_images/6_img_blob.png", img_blob)
cv2.imwrite("./filtered_images/7_img_numbered.png", img_num)