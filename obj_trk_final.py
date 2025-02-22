import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")
tracker=cv2._create()
ret,img=video.read()
box=cv2.selectROI("tracking",img,False)
tracker.init(img,box)

def drawbox(frame,box):
    x,y,w,h=int(box[0]),int(box[1]),int(box[2]),int(box[3])
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3,1)
    cv2.putText(frame,"Tracking",(75,90),cv2.FONT_HERSHEY_TRIPLEX,0.9,(0,0,255),3)


while True:
    check,img = video.read()  
    success,ball=tracker.update(img) 
    if success:
        drawbox(img,ball)
    else:
        cv2.putText(img,"LOST!!",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()
