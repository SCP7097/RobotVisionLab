import cv2

img = cv2.imread("../Intro_to_Images/test_image.png")
imageBlur=cv2.GaussianBlur(img,(155,155),0)

imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
cv2.imshow("Image blur", imageBlur)
cv2.waitKey(0)
