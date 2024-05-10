import cv2 as cv
import sys

img=cv.imread("../source/pooh.jpg")

t,bin_img=cv.threshold(img[:,:,2],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print("최적 임곗값=",t)

cv.imshow("R channel",img[:,:,2])
cv.imshow("R channel binarization",bin_img)

cv.waitKey()
cv.destroyAllWindows()
