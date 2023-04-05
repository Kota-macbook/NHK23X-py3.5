import pyrealsense2 as rs
import numpy as np
import cv2
import images4 as images3
import defs.line as line
import defs.H_change as H_c
from defs import phase
import math
#import H_filter as Hf
#import defs.H_middle as hm


Hue=19
Hue_wide=2
pole_num=80
checkdef=[0,0,0]

#コールバック用関数
def Hue_center_def(X):
    global Hue
    Hue=X
    checkdef[0]=1

def Hue_wide_def(X):
    global Hue_wide
    Hue_wide=X
    checkdef[1]=1

def pole_num_def(X):
    global pole_num
    pole_num=X
    checkdef[2]=1

#画像インポートまではネット上のサンプルコードを流用して行いました
#

# カメラの設定
conf = rs.config()
# RGB
conf.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
# 距離
#conf.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)

# stream開始
pipe = rs.pipeline()
profile = pipe.start(conf)

cnt = 0

#画質変更で落ちるならここ！
img_Hfil=cv2.imread("./programs/images/H_filter.png")
h,w=img_Hfil.shape[:2]
H_fil=H_c.change_H(h,w)
#H_fil=Hf.filter(img_Hfil)


#windowの設定
cv2.namedWindow("view1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("view1", 640, 480)

cv2.createTrackbar("Hue_center",
                   "view1",
                    19,
                    30,
                    Hue_center_def)


cv2.createTrackbar("Hue_wide",
                   "view1",
                    2,
                    10,
                    Hue_wide_def)

cv2.createTrackbar("Chose_poles",
                   "view1",
                    5,
                    10,
                    pole_num_def)

#cv2.setMouseCallback("Win_a",
#                    averages)

print("setup ended")

try:
    while True:
        """
        print(Hue)
        print(Hue_wide)
        print(pole_num)
        """
        frames = pipe.wait_for_frames()

        # frameデータを取得
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        # 画像データに変換
        img = np.asanyarray(color_frame.get_data())
        # 距離情報をカラースケール画像に変換する
        #depth_color_frame = rs.colorizer().colorize(depth_frame)
        #depth_image = np.asanyarray(depth_color_frame.get_data())

        #画像処理
        #img = cv2.imread("./test_images/de_pole4.png")

        #cv2.imwrite("./filtered_images/de_pole3.png", img)

        img2, lines ,stats,centroids = images3.images_4return(img,H_fil,Hue,Hue_wide)
#        img2 = images3.images_4return(img)

        #phases
        T_stats=list(stats.T)
        print("T_stats="+str(T_stats[1]))
        theta=phase.HighToTheta(T_stats[1].astype(int),int(h/2),0.674)
        #print(theta)
        #for i in range(theta.shape):
        #    print(math.degrees(theta[i]))

        #出力
        cv2.imshow("view1",img2)
        #print("End1")
        if cv2.waitKey(1) == 27:
            break
        cv2.destroyAllWindows

        
        #print("End 1frame")


except Exception as err:
    print("Error has occured.")
    print("type"+str(type(err)))
    print("args"+str(err.args))
    print("naiyopu"+str(err))
    print(err)