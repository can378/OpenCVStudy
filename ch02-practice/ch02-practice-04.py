import cv2 as cv
import sys

img=cv.imread("map.jpg")

if img is None:
    sys.exit("파일이 없습니다")


imgs=[img]*11

for i in range(1,11):
    imgs[i]=cv.resize(img,dsize=(0,0),fx=i/10,fy=i/10)
    cv.imwrite("resizeImg"+str(i)+".jpg",imgs[i])
    cv.imshow("resizeImg"+str(i),imgs[i])


cv.waitKey()
cv.destroyAllWindows()