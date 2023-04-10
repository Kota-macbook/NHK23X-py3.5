import pyrealsense2 as rs
import numpy as np
import cv2
import images4 as images3
import defs.H_change as H_c
from defs import phase
#import ReachAndPhase as RAP
#import H_filter as Hf
#import defs.H_middle as hm

#
Hue=19
Hue_wide=2
pole_num=80
checkdef=[0,0,0]

mode=0


#コールバック用関数
def Hue_center_def(X):
    global Hue
    global checkdef
    Hue=X
    checkdef[0]=1

def Hue_wide_def(X):
    global Hue_wide
    global checkdef
    Hue_wide=X
    checkdef[1]=1

def pole_num_def(X):
    global pole_num
    global checkdef
    pole_num=X
    checkdef[2]=1

def go_def(X):
    global mode
    mode=X


#画像インポートまではネット上のサンプルコードを流用して行いました



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












#H補正用画像
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

cv2.createTrackbar("Go!",
                   "view1",
                    0,
                    1,
                    go_def)


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
        #depth_frame = frames.get_depth_frame()
        # 画像データに変換
        img = np.asanyarray(color_frame.get_data())
        # 距離情報をカラースケール画像に変換する
        #depth_color_frame = rs.colorizer().colorize(depth_frame)
        #depth_image = np.asanyarray(depth_color_frame.get_data())


        print("import Ended")







        #画像処理
        img2, lines ,stats,centroids = images3.images_4return(img,H_fil,Hue,Hue_wide)





        print("images4 ended")



        """
        #phases
        stats_Y=list(stats.T)
        #print("T_stats="+str(stats_Y[1]))
        theta_Y=phase.HighToTheta(stats_Y[1].astype(int),int(h/2),0.674)
        #print(centroids.shape)
        stats_X=list(centroids.T)
        theta_X=phase.HighToTheta(stats_X[0].astype(int),int(w/2),0.674*(w/h))
        #print("("+str(theta_X)+","+str(theta_Y)+")")
        #for i in range(theta.shape):
        #    print(math.degrees(theta[i]))


        print("phase ended")

        """





        #出力
        cv2.imshow("view1",img2)
        #print("End1")
        if cv2.waitKey(1) == 27:
            break
        cv2.destroyAllWindows










except Exception as err:
    print("Error has occured.")
    print("type"+str(type(err)))
    print("args"+str(err.args))
    print("naiyopu"+str(err))