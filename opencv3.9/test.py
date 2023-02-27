import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv2.imread("./bushitu.png",0)

x = np.zeros((5,3,9),dtype = np.uint8)

for i in range(5):
    for j in range(3):
        for k in range(8):
            x[i][j][k] = i+ j + k
        
    
print(x[2][1][3])