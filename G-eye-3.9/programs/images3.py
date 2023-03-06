import cv2
import color_filter_X
import blob
import shirushi
import line
import numpy as np

def images_4return(img):
    h,w = img.shape[:2]
#    print("imread has ended")
    
    #ポールの色を抽出
    img2 = color_filter_X.color_filter_X(img, (14,117,89),(32,226,256))

    img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    print("color_filter has ended")


    #2値化
    border = 2
    ret, img3 = cv2.threshold(img3, border, 255, cv2.THRESH_BINARY)
    print("judge has ended")

    cv2.imwrite("./filtered_images/img_lines1.png",img3)

    #塊検出
    nLabels, img_no_use, stats, centroids= blob.blobs(img3,1000)
    print("blob has ended")

    #番号割り振り画像作成
    img = shirushi.shirushi(img,h,nLabels,stats,centroids)
    print("shirushi has ended")


    cv2.imwrite("./filtered_images/img_lines2.png",img)

    lines = np.zeros(1)

#    img, lines = line.lines(img,img3,h,w)
#    print("line has ended")

    return img, lines, stats, centroids



#img = cv2.imread("./test_images/camera4.png")
#img, lines ,stats, centroids = images(img)
#cv2.imwrite("./filtered_images/7_img_numbered.png", img)
#cv2.imshow("img",img)