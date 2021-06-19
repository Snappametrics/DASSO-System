import numpy as mynp
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    MyGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    MyGray = mynp.float32(MyGray)
    tdst = cv2.cornerHarris(MyGray,2,3,0.04)
    tdst = cv2.dilate(tdst,None)
    frame[tdst>0.01*tdst.max()]=[255,0,0]
    cv2.imshow('tdst',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
