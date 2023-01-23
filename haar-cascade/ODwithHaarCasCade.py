import cv2
import numpy as np
import time

object_cascade = cv2.CascadeClassifier('myhaar.xml')

cap = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    objects = object_cascade.detectMultiScale(gray,1.1,2)
    
    print(objects)
    
    for(x,y,w,h) in objects:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
    img = cv2.resize(img,(500,300))
    font = cv2.FONT_HERSHEY_SIMPLEX
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    
    fps= int(fps)
    fps = str(fps)
    
    cv2.putText(img,fps,(7,70),font,3,(100,255,0),3, cv2.LINE_AA)
        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
