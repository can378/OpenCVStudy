import cv2 as cv
import sys

cap=cv.VideoCapture(0,cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit("카메라 연결 실패")

isColor=True

while True:
    ret,frame=cap.read()
    
    if not ret:
        print("프레임 획득 실패. 루프 탈출")
        break
    
    if(isColor==False):
        frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        
    cv.imshow("Video display",frame)
    
    #key input////////////////////////////////////
    key=cv.waitKey(1)
    
    if key==ord('q'):
        break
    elif key==ord('c'):
        isColor=True
    elif key==ord('g'):
        isColor=False

    
        
    
    
cap.release()
cv.destroyAllWindows()
