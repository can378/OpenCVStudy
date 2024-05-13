import cv2 as cv
import sys

img=cv.imread("liquidCat.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다")

cv.rectangle(img, (10,30),(600,200),(0,0,255),2)

#글씨 쓰기
cv.putText(img,"cat",(830,24),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv.imshow("Draw",img)
cv.waitKey()
cv.destroyAllWindows()
