import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height = 250,350
# the four corner locations of the king card
pt1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# tells which point corresponds to which corner
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pt1,pt2)

imgOut = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("Out Image", imgOut)
cv2.waitKey(0)