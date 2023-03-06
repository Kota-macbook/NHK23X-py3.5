import cv2
import numpy as np
img = cv2.imread("./test_images/de_pole.png")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img2 = cv2.imread("./test_images/de_pole2.png")

img_hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

img3 = cv2.imread("./test_images/de_pole3.png")

img_hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

img4 = cv2.imread("./test_images/de_pole4.png")

img_hsv4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)

print("576,276")
print(img_hsv[276][576])

print("541,558")
print(img_hsv[558][541])

print("576,276")
print(img_hsv[276][576])


print("2-(415,270)")
print(img_hsv2[270][415])

print("2-(439,216)")
print(img_hsv2[216][439])

print("2-(436,273)")
print(img_hsv2[273,436])

print("2-(449,248)")
print(img_hsv2[248,449])

print("3-(408.226)")
print(img_hsv3[226,408])

print("4-(410,353)")
print(img_hsv4[353,410])

cv2.imshow("img",img4)
while True:
    if cv2.waitKey(30) == 27:
        break
cv2.destroyAllWindows

#270,415
#216,439
#273,436
#248,449