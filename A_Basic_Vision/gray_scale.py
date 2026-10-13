import cv2

img = cv2.imread("../Intro_to_Images/test_image.png")
imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
cv2.imshow("Image gray", imageGray)
cv2.waitKey(0)
