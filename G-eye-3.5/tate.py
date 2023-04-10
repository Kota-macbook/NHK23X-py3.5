import cv2
import numpy as np

arr1=np.arange(20).reshape(5,4)
print(arr1)

arr2=arr1.T
print(arr2)

arr3=np.where(arr2[1]<10)
print(arr1[arr3])

