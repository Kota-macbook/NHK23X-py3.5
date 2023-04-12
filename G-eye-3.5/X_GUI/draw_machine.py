import cv2
import numpy
import copy
import math
import numpy as np

img=cv2.imread("./X_GUI/map.png")
xy=[700,1400-150]
PI=int(math.degrees(math.pi/2))

def setX(X):
    global xy
    xy[0]=X

def setY(X):
    global xy
    xy[1]=X
def setPI(X):
    global PI
    PI=X

cv2.namedWindow("view1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("view1", 640, 480)

cv2.createTrackbar("X",
                   "view1",
                    xy[0],
                    1400,
                    setX)
cv2.createTrackbar("Y",
                   "view1",
                    xy[1],
                    1400,
                    setY)
cv2.createTrackbar("Phase",
                   "view1",
                    PI,
                    720,
                    setPI)



m_sizex=50.0
m_sizey=50.0
img_robo=cv2.imread("./X_GUI/rabbit.png")
h,w=img_robo.shape[:2]
size_image=(int(m_sizex*math.sqrt(2)+5),int(m_sizey*math.sqrt(2)+5),3)
h_r,w_r=(size_image[0],size_image[1])
robo=np.zeros(size_image,dtype=np.uint8)

while True:

    img_go=copy.deepcopy(img)
    center=(int(w/2),int(h/2))
    affine=cv2.getRotationMatrix2D(center,PI,1.0)
    affine[0][2]+=int(  (w_r-w)/2  )
    affine[1][2]+=int(  (h_r-h)/2  )
    robo=cv2.warpAffine(img_robo,affine,(w_r,h_r))


    cv2.imshow("view1",robo)
    if cv2.waitKey(10) == 27:
        break
    cv2.destroyAllWindows
