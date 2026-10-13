import cv2

cap=cv2.VideoCapture("test_video.mp4")
while True:
    success,img=cap.read()
    #image_blur=cv2.GaussianBlur(img,(15,15),sigmaX=0)
    #image_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if not success:
        break
    #cv2.imshow("video blur", image_blur)
    #cv2.imshow("video gray",image_gray)
    cv2.imshow("regular video",img)
    cv2.waitKey(1)