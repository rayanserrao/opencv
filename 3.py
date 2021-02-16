import cv2
import numpy as np

# load image
cap = cv2.VideoCapture(0) # 0 is for 1 st webcam, if u more number strt like 1, 2 etc 

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))  #- 3 is the proeprty to get width
    height = int(cap.get(4)) #- 4 is the property of height  

    image = np.zeros(frame.shape,np.uint8) 
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5) # shrinked to 4 peices as i shrinked heighta and width
    # image[:height//2,:width//2] = smaller_frame
    # image[height//2:,:width//2] = smaller_frame
    # image[:height//2,width//2:] = smaller_frame
    # image[height//2:,width//2:] = smaller_frame
    image[:height//2,:width//2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    image[height//2:,:width//2] = smaller_frame
    image[:height//2,width//2:] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    image[height//2:,width//2:] = smaller_frame

    
    cv2.imshow('image',image)
    if cv2.waitKey(1) == ord('q'): # ordinal value
        break

cap.release()
cv2.destroyAllWindows()