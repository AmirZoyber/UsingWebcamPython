#!/usr/bash/python3
# Author : AmirZyber
# You Can Find Me Here : 
#                        https://zil.ink/AmirZoyber

import cv2,time

# select which webcma to use (0 if you have just one webcam)
camera = cv2.VideoCapture(0)
# output format for recorded video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# path to save video
out = cv2.VideoWriter('output.avi',fourcc,24.0,(640,480))

ptime=0
while(True):
    ret, capture = camera.read()
    color = cv2.cvtColor(capture, cv2.COLOR_RGB2GRAY)
    out.write(capture)
    # calculating frame
    ctime = time.time()
    fps = 1 / (ctime-ptime)
    ptime = ctime
    # put text of frame on recording window
    cv2.putText(color,"FPS : %i"%(fps),(20, 70),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow("WEbCam",color)
    # it works until you press 'q' key on keybord
    if cv2.waitKey(1) == ord('q'):break
        
camera.release()
out.release()
cv2.destroyAllWindows()
