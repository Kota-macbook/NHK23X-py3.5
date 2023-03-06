import pyrealsense2 as rs
import numpy as np
import cv2
import images2
import line


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

#windowの設定
cv2.namedWindow("view1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("view1", 640, 480)

print("setup ended")

try:
    while True:
        frames = pipe.wait_for_frames()

        # frameデータを取得
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        # 画像データに変換
        img = np.asanyarray(color_frame.get_data())
        # 距離情報をカラースケール画像に変換する
        #depth_color_frame = rs.colorizer().colorize(depth_frame)
        #depth_image = np.asanyarray(depth_color_frame.get_data())

        print("End4")


        #画像処理
#        img = cv2.imread("./test_images/de_pole.png")

#        img2, lines ,stats,centroids = images2.images_4return(img)
        img2 = images2.images_4return(img)

        #出力
        cv2.imshow("view1",img2)
        if cv2.waitKey(30) == 27:
            break
        cv2.destroyAllWindows
        
        print("End 1frame")
        cv2.imwrite("./filtered_images/7_img_numbered.png", img)


except:
    print("Error has occured in 'import_realsense.py'.")