import cv2 as cv
import sys

img=cv.imread("map.jpg")
img2=cv.imread("liquidCat.jpg")

if img is None:
    sys.exit("img 파일을 찾을 수 없어")
if img2 is None:
    sys.exit("img2파일을 찾을 수 없어")
    
cv.imshow("Img1",img)
cv.imshow("Img2",img2)

cv.waitKey()
cv.destroyAllWindows()