import cv2 as cv
import numpy as np

img=cv.imread("../source/pooh.jpg")
img=cv.resize(img,dsize=(0,0),fx=0.4,fy=0.4)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.putText(gray,"pooh",(10,20),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

#Gaussian Blur
smooth=np.hstack((cv.GaussianBlur(gray,(5,5),0.0),cv.GaussianBlur(gray,(9,9),0.0),cv.GaussianBlur(gray,(15,15),0.0)))
cv.imshow("Gaussian",smooth)

#Median Blur
smooth2=np.hstack((cv.medianBlur(gray,5),cv.medianBlur(gray,9),cv.medianBlur(gray,15)))
cv.imshow("Median",smooth2)

#Gaussian + Median
Gaussian=cv.GaussianBlur(gray,(5,5),0.0)
smooth3=np.hstack((cv.medianBlur(Gaussian,5),cv.medianBlur(Gaussian,9),cv.medianBlur(Gaussian,15)))
cv.imshow("Gaussian+Median",smooth3)

cv.waitKey()
cv.destroyAllWindows()