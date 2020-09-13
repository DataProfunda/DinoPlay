import numpy as np
import pickle
import os 
from PIL import Image
import cv2
import pickle


#Pretrained Haar model
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0+ cv2.CAP_DSHOW)

while(True):
    
    #Capture frame from camera
    ret, frame = cap.read()
    
    #Color conversion to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Detect face 
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    
    for (x,y,w,h) in faces: 
        
        frame =  cv2.rectangle(frame, (x,y) , (x + w, y + h),  (255, 255, 0) , 2)
        
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
    
    