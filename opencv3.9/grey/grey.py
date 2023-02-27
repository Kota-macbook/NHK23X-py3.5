import cv2
import numpy as np
import matplotlib as mp

img = cv2.imread("./bushitu.png",0)

cv2.imwrite("grey.png",img)

# cv2.imshow("test",img)
# cv2.waitKey(1000)
# cv2.destroyAllWindows

print("The End")

print(img)

exit()