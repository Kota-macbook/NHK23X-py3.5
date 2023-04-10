import pyrealsense2 as rs
import numpy as np
import cv2
import images4 as images3
import defs.H_change as H_c
from defs import phase
import ReachAndPhase as RAP
from defs import movement as moves

#import H_filter as Hf
#import defs.H_middle as hm

Hue=19
Hue_wide=2
pole_num=80
checkdef=[0,0,0]

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
















#ここから本編

mode=0
Target=[0,0,0,0,0,0,0,0]
Target_type=[0,0,0,0,0,0,0,0]
P=0
I=0

try:
    while True:
        frames = pipe.wait_for_frames()
        # frameデータを取得
        color_frame = frames.get_color_frame()
        #depth_frame = frames.get_depth_frame()
        # 画像データに変換
        img = np.asanyarray(color_frame.get_data())
        # 距離情報をカラースケール画像に変換する
        #depth_color_frame = rs.colorizer().colorize(depth_frame)
        #depth_image = np.asanyarray(depth_color_frame.get_data()



        #画像処理
        img2, lines ,stats,centroids = images3.images_4return(img,H_fil,Hue,Hue_wide)
        #表示
        cv2.imshow("view1",img2)
        #print("End1")
        if cv2.waitKey(1) == 27:
            break
        cv2.destroyAllWindows


        #発射用
        if (mode==1 |mode==2) & Target[0]!=0:
            pole_top=[centroids[Target[0]][0],stats[Target[0]][1]]
            theta_X, Reach = RAP.RAP_def(pole_top,0.5,h,w)



            """
            movement=moves.phase(theta_X,I,D)
            move_Y.moving(movement)
            if I<A:
                if D<B:
                    mode=2
            #(While)などのループかもしれない
            if mode==2:
                go_amount=go.go_amo(Reach,Target_type([0]))
                Yasuda.go_pid(go_amount)

                for i in range(int(Target.shape[0])-1):
                    Target[i]=[i+1]
                    Target_type[i]=[i+1]

                Target[Target.shape[0]]=0
                Target_type[Target_type.shape[0]]=0
                mode=0



"""



except Exception as err:
    print("Error has occured.")
    print("type"+str(type(err)))
    print("args"+str(err.args))
    print("naiyopu"+str(err))