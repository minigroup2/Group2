import cv2
vidcap=cv2.VideoCapture('hello.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasframes,image=vidcap.read()
    if hasframes:
        cv2.imwrite("image"+str(count)+".png",image)
        return hasframes
sec=0
frameRate=0.1
count=1
success=getFrame(sec)
while success:
    count=count+1
    sec=sec+frameRate
    sec=round(sec,2)
    success=getFrame(sec)