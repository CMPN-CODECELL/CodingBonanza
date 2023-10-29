import cv2   #INCOMPLETE
import os
import numpy as np 

loc = r'../haarcascade_frontalface_default.xml'

face = cv2.CascadeClassifier(loc)
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 2)

    cv2.imshow("face", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
