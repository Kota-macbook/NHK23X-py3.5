import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#function "overstop"
def overstop(amount,small,large):
    if small>large:
        print("Error has occured at function 'overstop'")
        return -1
    if amount>large:
        amount=large
    if amount<small:
        amount=small
    return amount


def colorfilter(img, senter, haba):
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#ポールは(H, S, V)=(22.98, 188.84, 212) ただし、範囲は(0~180,0~255,0~255)

    low_H = int(23-haba[0])
    low_S = int(189-haba[1])
    low_V = int(212-haba[2])

    if low_H<0:
        low_H += 180
    low_S = overstop(low_S,0,255)
    low_V = overstop(low_V,0,255)
    lower = np.array([0,low_S,low_V])

    upper_H = int(23+haba[0])
    upper_S = int(119+haba[1])
    upper_V = int(212+haba[2])
    if upper_H>179:
       upper_H -= 180
    upper_S = overstop(upper_S,0,255)
    upper_V = overstop(upper_V,0,255)
    upper = np.array([150,upper_S,upper_V])

#if low_H>upper_H:
#    H_memory = low_H
#    low_H = upper_H
#upper_H = H_memory

    frame_mask = cv2.inRange(hsv, lower, upper)
    dst = cv2.bitwise_and(img,img,mask=frame_mask)

    img_filtered = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)

    return dst