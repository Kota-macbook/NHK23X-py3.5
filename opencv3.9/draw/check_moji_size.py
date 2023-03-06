import cv2
import numpy as np
import matplotlib as mp

img = np.ones((501,501,3),dtype=np.uint8)*255

#img = cv2.imread("./IMG_6071.JPG")

# print(img)

#print(np.shape(img))

#cv2.line(img,(13,0),(130,130),(0,0,0),5)

#cv2.line(img,(445,500),(395,445),(0,0,0),5)

#cv2.rectangle(img,(125,125),(400,450),(0,0,0),-1)

#cv2.line(img,(125,450),(400,125),(255,255,255),8)

#cv2.rectangle(img,(170,175),(355,400),(255,255,255),-1)

#cv2.circle(img,(303,240),30,(0,0,0),-1)

#cv2.ellipse(img,(303,239),(40,35),10,0,360,(0,0,0),5)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,"5",(-10,510),font,5,(255,0,0),1.5,cv2.LINE_AA)

cv2.imwrite("white.png",img)

cv2.imshow("img",img)
while True:
    if cv2.waitKey(30)==27:
        break
cv2.destroyAllWindows