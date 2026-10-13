from pickletools import uint8

import cv2
import cvzone
import numpy as np

img = cv2.imread("shapes.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgCanny = cv2.Canny(imgGray, 110, 100)
imgDilated=cv2.dilate(imgCanny, np.ones((3, 3), np.uint8),iterations=1)

imgStock = cvzone.stackImages([img, imgGray, imgCanny,imgDilated], 2, 2)

cv2.imshow("image", imgStock)
cv2.waitKey(0)
