
import cv2
import numpy as np

def beautiful(img1):

    #HSV
    imhsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

    #成分分解
    #im1h, im1s, im1v = cv2.split(imhsv1)
    im1h, im1s, im1v = cv2.split(img1)

    #ヒストグラム均一化
    eq1h = cv2.equalizeHist(im1h)
    eq1s = cv2.equalizeHist(im1s)
    eq1v = cv2.equalizeHist(im1v)

    #結合
    imgh = cv2.merge((eq1h,im1s,im1v))
    imgs = cv2.merge((im1h,eq1s,im1v))
    imgv = cv2.merge((im1h,im1s,eq1v))

    imghs = cv2.merge((eq1h, eq1s, im1v))
    imgsv = cv2.merge((im1h, eq1s, eq1v))
    imghv = cv2.merge((eq1h, im1s, eq1v))

    imghsv = cv2.merge((eq1h, eq1s, eq1v))

    #BGR
    imgh = cv2.cvtColor(imgh,cv2.COLOR_HSV2BGR)
    imgs = cv2.cvtColor(imgs,cv2.COLOR_HSV2BGR)
    imgv = cv2.cvtColor(imgv,cv2.COLOR_HSV2BGR)

    imghs = cv2.cvtColor(imghs,cv2.COLOR_HSV2BGR)
    imgsv = cv2.cvtColor(imgsv,cv2.COLOR_HSV2BGR)
    imghv = cv2.cvtColor(imghv,cv2.COLOR_HSV2BGR)

    imghsv = cv2.cvtColor(imghsv,cv2.COLOR_HSV2BGR)







    #一定化(別処理)
    hw_125 = np.ones(img1.shape[:2],dtype=np.uint8)*175

    img125s = cv2.merge((im1h, hw_125, im1v))
    img125v = cv2.merge((im1h, im1s, hw_125))

    img125sv = cv2.merge((im1h, hw_125, hw_125))

    img125s = cv2.cvtColor(img125s, cv2.COLOR_HSV2BGR)
    img125v = cv2.cvtColor(img125v, cv2.COLOR_HSV2BGR)
    img125sv = cv2.cvtColor(img125sv, cv2.COLOR_HSV2BGR)


    return imgh, imgs, imgv, imghs, imgsv, imghv, imghsv, img125s, img125v, img125sv


img1 = cv2.imread("./beautiful/de_pole1.png")

imgh, imgs, imgv, imghs, imgsv, imghv, imghsv, img125s, img125v, img125sv = beautiful(img1)

cv2.imwrite("./beautiful/return/H.png",imgh)
cv2.imwrite("./beautiful/return/S.png",imgs)
cv2.imwrite("./beautiful/return/V.png",imgv)
cv2.imwrite("./beautiful/return/HS.png",imghs)
cv2.imwrite("./beautiful/return/SV.png",imgsv)
cv2.imwrite("./beautiful/return/HV.png",imghv)
cv2.imwrite("./beautiful/return/HSV.png",imghsv)
cv2.imwrite("./beautiful/return/125S.png",img125s)
cv2.imwrite("./beautiful/return/125V.png",img125v)
cv2.imwrite("./beautiful/return/125SV.png",img125sv)