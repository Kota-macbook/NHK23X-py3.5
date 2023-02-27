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



img = cv2.imread("./bushitu.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


haba_H = 20
haba_S = 100
haba_V = 100


#ポールは(H, S, V)=(22.98, 188.84, 212) ただし、範囲は(0~180,0~255,0~255)

low_H = int(23-haba_H)
low_S = int(189-haba_S)
low_V = int(212-haba_V)

if low_H<0:
    low_H += 180
low_S = overstop(low_S,0,255)
low_V = overstop(low_V,0,255)
lower = np.array([0,low_S,low_V])

upper_H = int(23+haba_H)
upper_S = int(119+haba_S)
upper_V = int(212+haba_V)
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

cv2.imwrite("./chose_color/filtered.png", img_filtered)
cv2.imwrite("./chose_color/filtered2.png", dst)

print(img.shape)
print(img_filtered.shape)
print(dst.shape)

print(low_H,low_S,low_V)
print(upper_H,upper_S,upper_V)