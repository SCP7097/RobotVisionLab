import cvzone
from  cvzone.Utils import *

img = cv2.imread("shapes.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgCanny = cv2.Canny(imgGray, 20, 50)
imgDilated=cv2.dilate(imgCanny, np.ones((3, 3), np.uint8),iterations=1)

imgContour,conFound=findContours(img,imgDilated,filter=None,drawCon=True)


imgStock = cvzone.stackImages([imgGray,imgDilated,imgContour], 2, 0.5)

cv2.imshow("image", imgStock)



cv2.waitKey(0)
