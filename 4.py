import cv2
import numpy as np

# load image
cap = cv2.VideoCapture(0) # 0 is for 1 st webcam, if u more number strt like 1, 2 etc 

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))  #- 3 is the proeprty to get width
    height = int(cap.get(4)) #- 4 is the property of height  
    
    img = cv2.line(frame, (0,0),(width,height), (255,0,0),10)
    img = cv2.line(img, (0,height),(width,0), (0,255,0),5)
    img = cv2.rectangle(img,(100,100),(200,200),(135,135,135),5)
    img = cv2.rectangle(img,(100,100),(200,200),(135,135,135),-1) # itn will fill auomatcilaly entire rectangle
    img = cv2.circle(img,(300,300),60, (0,255,255),-1)

    font = cv2.FONT_HERSHEY_SIMPLEX   #(u can pick any of those from suggestions) and check for the documentation how to write)

    img = cv2.putText(img,'rayan is great',(200, height - 10), font, 4, (0,0,0),5,cv2.LINE_AA)


    
    cv2.imshow('image',img)
    if cv2.waitKey(1) == ord('q'): # ordinal value
        break

cap.release()
cv2.destroyAllWindows()