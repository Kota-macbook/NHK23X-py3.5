import cv2


def shirushi(img_num,h,nLabels,stats,centroids):
    for i in range(1, nLabels):
        #重心
        xc = int(centroids[i][0])
        yc = int(centroids[i][1])

        haba = stats[i][2]
        takasa = stats[i][3]

        hidariue = [stats[i][0],stats[i][1]]
        migishita = [stats[i][0]+haba,stats[i][1]+takasa]

        font = cv2.FONT_HERSHEY_COMPLEX
        r1 = haba/4
        r2 = int(r1)
        scale = int(r1/20)
        color = (0, 0,0)

        #print(stats.shape)
        #print(migishita)
        cv2.rectangle(img_num,hidariue,migishita,(0,0,0),2)
        cv2.circle(img_num, (xc,yc), r2,(255,0,255),-1)
        if xc-60>=0 and yc+60<=h:
            cv2.putText(img_num, str(i), (xc-10,yc+10), font, scale, color, 2, cv2.LINE_AA)
        else:
            cv2.putText(img_num, str(i), (xc,yc), font, scale, color, 2, cv2.LINE_AA)
    return img_num