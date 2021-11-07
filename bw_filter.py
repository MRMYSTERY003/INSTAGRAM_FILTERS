import cv2 
import numpy as np


video = cv2.VideoCapture(0)

while True:
    _,img = video.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('original',img)
    cv2.imshow('gray',gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
