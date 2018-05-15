import numpy as np
import cv2 as cv

cap = cv.VideoCapture('work.flv')
while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == False:
        print("end of stream")
        break
    
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #cut frame [y1:y2, x1:x2]
    crop_img = frame[0:100, 0:200]
    #

    cv.imshow('frame',crop_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()