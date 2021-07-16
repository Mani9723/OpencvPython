import cv2
import numpy as np
img = cv2.imread("Resources/lena.png")
kernel = np.ones((1,5),np.uint8) # 1x5 identity matrix

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # gray scale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # gaussian blur
imgCanny = cv2.Canny(img,150,200) # Edge Detection
# dilated image aka the thickness of the edges
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
# make the edges thinner
imgErode = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Grey Image",imgGray) # gray scale
cv2.imshow("GBlur Image",imgBlur) # gaussian blur
cv2.imshow("Canny Image",imgCanny) # Canny blur
cv2.imshow("Dilated Image",imgDilation) #  dilated Image
cv2.imshow("Eroded Image",imgErode) #  eroded Image
cv2.waitKey(0);