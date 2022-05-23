#!/usr/bash/python3
# Author : AmirZyber
# You Can Find Me Here : 
#                        https://zil.ink/AmirZoyber

import cv2,time
camera = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,24.0,(640,480))
ptime=0
while(True):
    ret, capture = camera.read()
    color = cv2.cvtColor(capture, cv2.COLOR_RGB2GRAY)
    out.write(capture)
    ctime = time.time()
    fps = 1 / (ctime-ptime)
    ptime = ctime
    cv2.putText(color,"FPS : %i"%(fps),(20, 70),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow("WEbCam",color)
    if cv2.waitKey(1) == ord('q'):break
camera.release()
out.release()
cv2.destroyAllWindows()