import numpy as np
import cv2
import random

# Load the cascade
face_cascade = cv2.CascadeClassifier('F:\\project\\insta filetrs\\Face_detection\\data.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

BLACK = (255,255,255)
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 1.3
font_color = BLACK
font_thickness = 3
text = 'Your soulmate name'


counts = 50
i = 0


while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if i > counts:
        letter = letter
    else:
        i += 1
        letter = Letters[random.randint(0,25)]
    

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        col = (random.randint(0,255), random.randint(0,255), random.randint(0,255),)
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        img = cv2.putText(img, text, (x-int(w/3),y), font, font_size, font_color, font_thickness, cv2.LINE_AA)
        img = cv2.putText(img, letter, (x+int(w/2),y+int(h/4)), font, font_size, col, font_thickness, cv2.LINE_AA)


    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(10) & 0xff

    if k == ord('q'):
        break
        
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()