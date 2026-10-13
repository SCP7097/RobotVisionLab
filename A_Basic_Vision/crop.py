import cv2

img = cv2.imread("../Intro_to_Images/test_image.png")

# [y1:y2,x1:x2]
imageCrop = img[50:640, 280:550]

cv2.imshow("Image", img)
cv2.imshow("Image crop", imageCrop)
cv2.waitKey(0)
