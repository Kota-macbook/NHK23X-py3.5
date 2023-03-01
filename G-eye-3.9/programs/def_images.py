import cv2
from cv2 import threshold
#import numpy as np
#import math
#自作関数、場所は./programs/def_colorfilter.py
import def_colorfilter
import blob
#import addition_img
import shirushi
#import copy

def images(img):
    #画像をインポート
    img = cv2.imread("./test_images/pole.png")
    h,w = img.shape[:2]
    print("imread has ended")
    
    #ポールの色を抽出
    img2 = def_colorfilter.colorfilter(img,(23,189,212),(4, 61, 108))
    img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    print("color_filter has ended")

    #ノイズキャンセル
    #img_bi = cv2.bilateralFilter(img_Gray, 30, 30, 200)

    #2値化
    border = 103
    ret, img3 = cv2.threshold(img3, border, 255, cv2.THRESH_BINARY)
    print("judge has ended")

    #塊検出
    nLabels, img3, stats, centroids= blob.blobs(img3,20000)
    print("blob has ended")

    #番号割り振り画像作成
    #img_num = copy.deepcopy(img)
    img = shirushi.shirushi(img,h,nLabels,stats,centroids)
    print("shirushi has ended")

    return img
    #img_numbered = addition_img.addition_img(img,img_blob)
        

img = cv2.imread("./test_images/bushitu.png")
img = images(img)
cv2.imwrite("./filtered_images/7_img_numbered.png", img)