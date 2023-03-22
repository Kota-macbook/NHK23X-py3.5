import cv2
import numpy as np
import math

def change_H(img):
#    Hi=0.034439

    h,w = img.shape[:2]

    img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    H,S,V=cv2.split(img2)
    HF=H.astype(np.float32)

    border1=w*250/1280
    border2=w*780/1280

    ran = np.arange(1,w+1).reshape(1,w)
    ran2 = np.where(ran<=border1,3-ran*3/border1,ran)
    ran2 = np.where(ran2>=border2,((ran2-border2)*4)/(w-border2),ran)
    ran2 = np.where((ran2>border1) & (ran2<border2),0,ran)
#    print(ran2)
    print(border2)
    HF+=ran2
    print(border1)

    H_Re=HF.astype(np.uint8)

    img2=cv2.merge((H_Re,S,V))

    img3=cv2.cvtColor(img2,cv2.COLOR_HSV2BGR)

    return H_Re

img = np.ones((780,1280,3),dtype=np.uint8)*255

img2=change_H(img)

cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.resizeWindow("img",410,370)

cv2.imshow("img",img2)
cv2.waitKey(0)
cv2.destroyAllWindows