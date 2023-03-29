import cv2
import numpy as np
import math

def change_H(img):
#    Hi=0.034439

    h,w = img.shape[:2]

    img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    H,S,V=cv2.split(img2)
    #H-=100
    HF=H.astype(np.float32)

    border1=int(w*250/1280)
    border2=int(w*780/1280)

    ran = np.arange(1,w+1).reshape(1,w)
#    print(ran)
    ran2 = np.where(ran<=border1,3-ran*3/border1,ran)
    ran3 = np.where(ran>=border2,((ran-border2)*6)/(w-border2),ran2)
    ran4 = np.where((ran>border1) & (ran<border2),0,ran3)
#    print(ran2)
    print(border2)
    HF+=ran4
    print(border1)

    H_Re=HF.astype(np.uint8)

    img2=cv2.merge((H_Re,S,V))

    img3=cv2.cvtColor(img2,cv2.COLOR_HSV2BGR)

    return H_Re

#img = np.ones((720,1280,3),dtype=np.uint8)*100

#img2=change_H(img)

#cv2.namedWindow("img",cv2.WINDOW_NORMAL)
#cv2.resizeWindow("img",410,370)

#cv2.imshow("img",img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows