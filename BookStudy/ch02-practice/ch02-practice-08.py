import cv2 as cv
import sys
import math

img=cv.imread("map.jpg")

if img is None:
    sys.exit("no file")


# draw func///////////////////
def draw(event,x,y,flags,param):
    global ix,iy    
    
    #RECTANGLE
    if event==cv.EVENT_LBUTTONDOWN:
        ix,iy=x,y
    elif event==cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix,iy),(x,y),(29,230,181),2)
        
    #CIRCLE
    elif event==cv.EVENT_RBUTTONDOWN:
        ix,iy=x,y
    elif event==cv.EVENT_RBUTTONUP:
        r=math.sqrt(((x-ix)**2)+((y-iy)**2))
        cv.circle(img,(ix,iy),int(r),(234,217,153),2)
        
    cv.imshow("Drawing",img)



#show///////////////////////////
cv.namedWindow("Drawing")
cv.imshow("Drawing",img)

cv.setMouseCallback("Drawing",draw)



while(True):
    if cv.waitKey(1)==ord("q"):
        cv.destroyAllWindows()
        break