import cv2
from cv2 import threshold
import numpy as np
import math
#自作関数、場所は./programs/def_colorfilter.py
import def_colorfilter
import blob
import addition_img
import copy

#画像をインポート
img = cv2.imread("./test_images/pole.png")
h,w = img.shape[:2]
#ポールの色を抽出
img_colorfiltered = def_colorfilter.colorfilter(img,(23,189,212),(4, 61, 108))
img_Gray = cv2.cvtColor(img_colorfiltered, cv2.COLOR_BGR2GRAY)

#ノイズキャンセル
#img_bi = cv2.bilateralFilter(img_Gray, 30, 30, 200)

#2値化
border = 103
ret, img_judged = cv2.threshold(img_Gray, border, 255, cv2.THRESH_BINARY)

#塊検出
nLabels, img_blob, stats, centroids= blob.blobs(img_judged,20000)

#番号割り振り画像作成
img_num = img

print(nLabels)

for i in range(1, nLabels):
    xc = int(centroids[i][0])
    yc = int(centroids[i][1])
    
    font = cv2.FONT_HERSHEY_COMPLEX
    scale = 5
    color = (0, 0,0)
    
    print(stats.shape)
    
    hidariue = [stats[i][0],stats[i][1]]
    migishita = [stats[i][0]+stats[i][2],stats[i][1]+stats[i][3]]
    print(migishita)
    cv2.rectangle(img_num,hidariue,migishita,(0,0,0),5)
    cv2.circle(img_num, (xc,yc), 75,(255,0,255),-1)
    if xc-60>=0 and yc+60<=h:
        cv2.putText(img_num, str(i), (xc-60,yc+60), font, scale, color, 4, cv2.LINE_AA)
    else:
        cv2.putText(img_num, str(i), (xc,yc), font, scale, color, 4, cv2.LINE_AA)

    

#img_numbered = addition_img.addition_img(img,img_blob)



cv2.imwrite("./filtered_images/1_img.png", img)
cv2.imwrite("./filtered_images/2_img_color.png", img_colorfiltered)
cv2.imwrite("./filtered_images/3_img_Gray.png", img_Gray)
#cv2.imwrite("./filtered_images/4_img_bi.png", img_bi)
cv2.imwrite("./filtered_images/5_img_judged.png", img_judged)
cv2.imwrite("./filtered_images/6_img_blob.png", img_blob)
cv2.imwrite("./filtered_images/7_img_numbered.png", img_num)


