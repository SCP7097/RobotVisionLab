import cv2
import cvzone
import random

from cvzone.ColorModule import ColorFinder

cap = cv2.VideoCapture(0)

myColorFinder=ColorFinder(trackBar=False)
hsvValue={'hmin': 38, 'smin': 36, 'vmin': 0, 'hmax': 83, 'smax': 255, 'vmax': 255}

while True:


    success, img = cap.read()
    if not success:
        break

    imgColor, mask = myColorFinder.update(img, hsvValue)
    imgStack = cvzone.stackImages([img, imgColor, mask], 3, 0.5)


    cv2.imshow("color detection", imgStack)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


    """"
    ↑basically means that when key is pressed and key("q") is the one inside
    the parenthesis the following code will be executed. If not then it will 
    wait for 1 ms
    """
