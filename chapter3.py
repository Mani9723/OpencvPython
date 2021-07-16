import cv2
import numpy as np

img = cv2.imread("Resources/lambo.PNG")
print(img.shape)

imgResize = cv2.resize(img,(200,200)) #dsize = (width,height)
print(imgResize.shape)

imgCropped = img[0:200,200:500] # cropping requires (height,width)


cv2.imshow("Resized image",img)
cv2.imshow("Resized image1",imgResize)
cv2.imshow("Cropped image2",imgCropped)
cv2.waitKey(0)
