import numpy as np
import cv2 

cap=cv2.VideoCapture(0)

while 1:
    _,frame= cap.read()
    cv2.imshow('rgb', frame)

    k=cv2.waitKey(5)
    if k==27:
        break

cv2.destroyAllWindows()
