import cv2
import numpy as np

img=np.ones((720,1280,3),dtype=np.uint8)*128

img=np.array(img)
img2=cv2.rectangle(img,(600,320),(680,400),(255,255,255),2)

cv2.imwrite("./test.png",img2)