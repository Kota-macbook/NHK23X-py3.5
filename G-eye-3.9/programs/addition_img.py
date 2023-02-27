import cv2
import numpy as np

def addition_img(img1,img_Gray):
    h,w = img1.shape[:2]
#    img_con2_1=np.zeros((h,w,3),dtype=np.uint8)
    img_con = img1.astype(np.uint16)
    img_con2 = img_Gray.astype(np.uint16)
    
    for i in range(h):
        for j in range(w):
            img_con[i][j] += img_con2[i][j]
    
    
    
#    print(img_con.shape)
#    print(img_con2.shape)
    
    img_con4=np.clip(img_con,a_min=0,a_max=255)

    img_con5=img_con4.astype(np.uint8)

#    cv2.imwrite("./filtered_images/7_img_numbered.png", img_numbered)
    return img_con5

img1=cv2.imread("./1_img.png")
img2=cv2.imread("./6_img_blob.png",0)

img3=addition_img(img1,img2)

cv2.imwrite("./addition.png",img3)