import cv2
import color_filter_X
import test_images.blob as blob
import shirushi
import line
import numpy as np
#import save_deta.H_change as H_change

def images_4return(img,H_fil):
    #setup
    h,w = img.shape[:2]
    img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img_Blur=cv2.blur(img,(3,3))
    H,S,V=cv2.split(img_HSV)
    

    



    
    #img_H = H_change.change_H(img,Hi=0.057177615)
#default 0.034439

    cv2.imwrite("./filtered_images/de_pole4.png", img)

#    return img_H,0,0,0

    #ポールの色を抽出
    img2 = color_filter_X.color_filter_X(img, (17,100,100),(19,255,255))

    img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    print("color_filter has ended")

    #return img3,0,0,0

    #2値化
    border = 2
    ret, img3 = cv2.threshold(img3, border, 255, cv2.THRESH_BINARY)
    print("judge has ended")

    cv2.imwrite("./filtered_images/img_lines1.png",img3)

    #塊検出
    nLabels, img_no_use, stats, centroids= blob.blobs(img3,1000)
    print("blob has ended")

    #img=line.lines(img,img3,h,w)

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