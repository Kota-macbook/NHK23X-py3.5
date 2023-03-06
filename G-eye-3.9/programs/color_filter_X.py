import numpy
import cv2
def color_filter_X(img,smaller,bigger):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    frame_mask = cv2.inRange(hsv,smaller,bigger)
    dst = cv2.bitwise_and(img,img,mask=frame_mask)
    return dst

#img = cv2.imread("./test_images/de_pole.png")
#img2 = color_filter_X(img, (17,77,102),(21,237,162))

#(19,157,132),(2,80, 30)
#cv2.imshow("img",img2)
#while True:
#    if cv2.waitKey(30) == 27:
#        break
#cv2.destroyAllWindows
