import cv2
import cvzone
import random

from cvzone import findContours
from cvzone.ColorModule import ColorFinder

cap = cv2.VideoCapture(0)

myColorFinder=ColorFinder(trackBar=False)
hsvValue1={'hmin': 38, 'smin': 36, 'vmin': 0, 'hmax': 83, 'smax': 255, 'vmax': 255}
hsvValue2={'hmin': 14, 'smin': 130, 'vmin': 150, 'hmax': 27, 'smax': 255, 'vmax': 255}
while True:


    success, img = cap.read()
    if not success:
        break

    imgColor1, mask1 = myColorFinder.update(img, hsvValue1)
    imgColor2, mask2 = myColorFinder.update(img, hsvValue2)
    imgContours1,confound1=findContours(img,mask1)
    imgContours2, confound2 = findContours(img, mask2)
    imgStack = cvzone.stackImages([img, imgColor1, mask1,imgContours1], 3, 0.5)


    cv2.imshow("color detection", imgStack)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


    """"
    ↑basically means that when key is pressed and key("q") is the one inside
    the parenthesis the following code will be executed. If not then it will 
    wait for 1 ms
    """
