import cv2 as cv
import sys

img=cv.imread("map.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다")

#SQUARE
cv.rectangle(img, (150,150),(300,300),(0,0,255),2)

#TEXT
cv.putText(img,"cat",(100,100),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

#ARROW
cv.arrowedLine(img,(125,100),(150,150),(255,0,0),2)

#SHOW
cv.imshow("Draw",img)

cv.waitKey()
cv.destroyAllWindows()
