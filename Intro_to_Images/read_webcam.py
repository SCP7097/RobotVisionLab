import cv2
import random

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    if not success:
        break
    #webcam_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.putText(img, "This is from your computer camera", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)
    cv2.imshow("video regular", img)
    #cv2.imshow("video gray",webcam_gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    """"
    ↑basically means that when key is pressed and key("q") is the one inside
    the parenthesis the following code will be executed. If not then it will 
    wait for 1 ms
    """
