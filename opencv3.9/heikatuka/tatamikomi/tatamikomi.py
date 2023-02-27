import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# img = cv2.imread("./bushitu.png",0)

img = np.zeros((1000,1000))

for i in range(30000):
    
    x = np.random.randint(100,900)
    
    y = np.random.randint(100,900)
    
    img[x,y] = 255

average_kernel = np.ones((9,9))/81.0

img_ave = cv2.filter2D(img,-1,average_kernel)

cv2.imwrite("./heikatuka/tatamikomi/noise.png", img)

cv2.imwrite("./heikatuka/tatamikomi/filtered.png", img_ave)