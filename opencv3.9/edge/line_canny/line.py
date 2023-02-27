import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#edge抽出

img_Color = cv2.imread("./line_circle.jpg")

img_G = cv2.cvtColor(img_Color,cv2.COLOR_BGR2GRAY)

h,w = img_G.shape[:2]

h_50 = h/6

w_50 = w/6

h_w_large = (h_50 + w_50)/2

h_w_noise = h_w_large/2

img_canny = cv2.Canny(img_G,h_w_noise,h_w_large)

cv2.imwrite("./edge/line_canny/Canny.png",img_canny)


#lineを弾く


lines = cv2.HoughLines((img_canny),1,np.pi/180,150)

# i = [ [[rho0 theta0]] [[rho1 theta1]] ... ] 二重括弧のため　i[0][0]

for i in lines[:]:
    
    rho = i[0][0]
    theta = i [0][1]
    
    a = np.cos(theta)
    b = np.sin(theta)
    
    X0 = rho * a
    Y0 = rho * b
    
    X1 = int( X0 - (-1000 * b) )
    Y1 = int( Y0 - (1000 * a) )
    
    X2 = int( X0 + (-1000 * b) )
    Y2 = int( Y0 + (1000 * a) )
    
    cv2.line(img_Color,(X1,Y1),(X2,Y2),(255,0,0),1)
    
cv2.imwrite("./edge/line_canny/lined_img.png",img_Color)

