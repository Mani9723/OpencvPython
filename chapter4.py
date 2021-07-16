import cv2
import numpy as np

# 0 = black
img = np.zeros((512,512,3),np.uint8)
#print(img.shape)
#img[200:300,100:200] = 255,0,0 # color whole/parts of image

#                   img.shape returns array,[0]=height,shape[1]=width
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),5) # green diagonal line
cv2.rectangle(img,(0,0),(300,300),(255,0,0),cv2.FILLED) # fills rectangle
cv2.circle(img,(400,50),30,(0,0,255),cv2.FILLED) # Circle filled
cv2.putText(img,"Betty's puss",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(150,200,255),1) # adding text



cv2.imshow("Black Image",img)
cv2.waitKey(0)
