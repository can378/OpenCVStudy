import cv2 as cv
import numpy as np
import time

img=cv.imread("../source/pooh.jpg")

if img is None:
    print("img is null")
    
def my_cvtGray1(bgr_img):
    g=np.zeros([bgr_img.shape[0],bgr_img.shape[1]])
    for r in range(bgr_img.shape[0]):
        for c in range(bgr_img.shape[1]):
            g[r,c]=0.114*bgr_img[r,c,0]+0.587*bgr_img[r,c,1]+0.299*bgr_img[r,c,2]
    return np.uint8(g)

def my_cvtGray2(bgr_img):
    g=np.zeros([bgr_img.shape[0],bgr_img.shape[1]])
    g=0.114*bgr_img[:,:,0]+0.587*bgr_img[:,:,1]+0.299*bgr_img[:,:,2]
    return np.uint8(g)



start=time.time()
my_cvtGray1(img)
print("for time:",time.time()-start)

start=time.time()
my_cvtGray2(img)
print("array tim:",time.time()-start)

start=time.time()
cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print("OpenCV time:",time.time()-start)
