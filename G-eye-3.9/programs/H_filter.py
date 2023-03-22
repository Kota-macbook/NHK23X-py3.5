import cv2
import numpy as np
import math

def filter(img):

    h,w = img.shape[:2]
#    img=cv2.blur(img,(3,3))
    img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    H,S,V=cv2.split(img_HSV)

    H_ave=np.mean(H,dtype=np.int16)

    H_fil=H_ave-H

    return H_fil
