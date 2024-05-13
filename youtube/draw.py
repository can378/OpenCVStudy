import cv2 as cv
import numpy as np

#blank canvas
blank=np.zeros((500,500,3),dtype='uint8')
blank[200:300,300:400]=0,255,0
cv.imshow('Green',blank)

#draw square
# cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=cv.FILLED)
# cv.rectangle(blank,(0,0),(250,300),(0,255,0),thickness=3)
# cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=-1)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
cv.imshow('Rectangle',blank)


#draw circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('circle',blank)


#draw line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('line',blank)


#write text
cv.putText(blank,'Hello',(0,225),cv.FONT_HERSHEY_TRIPLEX, 1.0,(255,200,0),2)
cv.imshow('Text',blank)


cv.waitKey(0)