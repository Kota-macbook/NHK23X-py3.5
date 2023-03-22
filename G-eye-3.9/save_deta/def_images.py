import cv2
from cv2 import threshold
#import numpy as np
#import math
#自作関数、場所は./programs/def_colorfilter.py
import def_colorfilter
import test_images.blob as blob
#import addition_img
import shirushi
#import copy
import line

def images(img):
    #画像をインポート
#    img = cv2.imread("./test_images/pole.png")
    h,w = img.shape[:2]
    print("imread has ended")

#    img = cv2.GaussianBlur(img, (3,3), 2)

#    img = cv2.bilateralFilter(img, 30, 30, 200)

    
    #ポールの色を抽出
    img2 = def_colorfilter.colorfilter(img,(20,181,138),(2, 61, 108))
    #darkness=[0, 0, 0]
    #whiteness=[80, 72, 140]
    
    #return img
    img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    print("color_filter has ended")

   # ノイズキャンセル
    #img3 = cv2.bilateralFilter(img3, 30, 30, 200)

    #2値化
    border = 100
    ret, img3 = cv2.threshold(img3, border, 255, cv2.THRESH_BINARY)
    print("judge has ended")
#    return img3

    #塊検出
    nLabels, img3, stats, centroids= blob.blobs(img3,1000)
    print("blob has ended")

#    return img3

    #番号割り振り画像作成
    #img_num = copy.deepcopy(img)
    img = shirushi.shirushi(img,h,nLabels,stats,centroids)
    print("shirushi has ended")

    img, lines = line.lines(img,img3,h,w)
#    print("line has ended")

    return img, lines, stats, centroids
    #img_numbered = addition_img.addition_img(img,img_blob)
        

#img = cv2.imread("./test_images/bushitu.png")
#img, lines ,stats, centroids = images(img)
#cv2.imwrite("./filtered_images/7_img_numbered.png", img)
#cv2.imshow("img",img)