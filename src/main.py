
#!/usr/bin/env python

import numpy as np
import cv2 as cv
from dominantColor import dominantColor

class ParkingSpace():
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.emtpy = True

    def getCrop(self, frame):
        return frame[self.y1:self.y2, self.x1:self.x2]

parkingSpaces = [ParkingSpace(808, 886, 469, 527)]



cap = cv.VideoCapture('../work.flv')
while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == False:
        print("end of stream")
        break
    
    for pSpace in parkingSpaces:
        dcolor = dominantColor(pSpace.getCrop(frame))
        cv.rectangle(frame, (pSpace.x1, pSpace.y1), (pSpace.x2, pSpace.y2),
		(dcolor[0], dcolor[1], dcolor[2]), -1)
    #cut frame [y1:y2, x1:x2]
    #crop_img = frame[469:527, 808:886]
    #

    cv.imshow('frame',frame)
    #cv.imshow('crop',crop_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()