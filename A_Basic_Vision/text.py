import cv2

img = cv2.imread("../Intro_to_Images/test_image.png")
# [y1:y2 , x1:x2]
imageCrop = img[50:640, 280:550].copy()

# 替换为合法字体，加上抗锯齿 LINE_AA
cv2.putText(imageCrop, "This is a dog", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 255), 2)

cv2.putText(img, "This is a dog running on the lawn", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (240, 200, 123), 2)

cv2.imshow("Image text",img)
cv2.imshow("cropped Image text", imageCrop)
cv2.waitKey(0)

