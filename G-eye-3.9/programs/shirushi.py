import cv2

def shirushi(img_num,h,nLabels,stats,centroids):
    for i in range(1, nLabels):
        xc = int(centroids[i][0])
        yc = int(centroids[i][1])
    
        font = cv2.FONT_HERSHEY_COMPLEX
        scale = 5
        color = (0, 0,0)
    
        print(stats.shape)
    
        hidariue = [stats[i][0],stats[i][1]]
        migishita = [stats[i][0]+stats[i][2],stats[i][1]+stats[i][3]]
        print(migishita)
        cv2.rectangle(img_num,hidariue,migishita,(0,0,0),5)
        cv2.circle(img_num, (xc,yc), 75,(255,0,255),-1)
        if xc-60>=0 and yc+60<=h:
            cv2.putText(img_num, str(i), (xc-60,yc+60), font, scale, color, 4, cv2.LINE_AA)
        else:
            cv2.putText(img_num, str(i), (xc,yc), font, scale, color, 4, cv2.LINE_AA)
    return img_num