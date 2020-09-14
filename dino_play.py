import numpy as np
import pickle
import os 
from PIL import Image
import cv2
import pickle
from pyautogui import press, typewrite, hotkey
import time
from selenium import webdriver

#Open new tab with Dino game.
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://chromedino.com/")


#Pretrained Haar model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml') 


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
        
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 
        
        #Detect smile
        smiles = smile_cascade.detectMultiScale(roi_gray, 2 , 30)
        
        smile_detected = False
          
        for (sx, sy, sw, sh) in smiles: 
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2) 
            smile_detected = True
        
        if(smile_detected):
            press('up')
  
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
    
    
