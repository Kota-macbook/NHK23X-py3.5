import cv2
import numpy as np
#import copy

def blobs(img_G,upper):
    
    nLabels, labelImages, stats, centroids = cv2.connectedComponentsWithStats(img_G)
    print("blob1 has ended")

    print(stats)
    
    nLab2 = 0
    
    for i in range(nLabels):
        if stats[i][-1]>upper:
            nLab2 += 1
    print("blob2 has ended")
    
    #print(nLab2-1)
            
    h,w = img_G.shape[:2]
    
    img_return = np.zeros((h,w),dtype = np.uint8)
    print("blob3 has ended")

    #uintは場合に応じて変える
    cent2=np.zeros((nLab2,2),dtype=np.uint16)
    stats2=np.zeros((nLab2,5),dtype=np.uint16)
    labI2=np.ones((nLab2),dtype=np.int16)
    
    print("blob4 has ended")

    
    labI2[0]=-1
    
    con = 1
    
    for i in range(1,nLabels):
        if stats[i][-1]>upper:
            cent2[con]=centroids[i]
            stats2[con]=stats[i]
            labI2[con]=i
            con+=1
    
#    for x in range(w):
#        for y in range(h):
#            for z in labI2:
#                if labelImages[y,x] == z :
#                    img_return[y,x]=255
#
#    print("blob6 has ended")
    print(stats2)
    
    return nLab2, img_return, stats2, cent2
        
            
            
        
    
    
    
    
    

#img = cv2.imread("./filtered_images/5_img_judged.png",0)

#nLabels, labelImages, stats, centroids = blobs(img, 250000)



#cv2.imwrite("./test.png",labelImages)