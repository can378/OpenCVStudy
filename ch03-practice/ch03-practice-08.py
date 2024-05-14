import cv2 as cv
import numpy as np
import time



def myEqualizeHist(image):
    # 이미지를 그레이스케일로 변환
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    # 이미지의 히스토그램 계산
    hist, bins = np.histogram(gray_image.flatten(), 256, [0,256])
    
    # 누적 분포 함수(CDF) 계산
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    # 원본 이미지에 대한 누적 분포 함수의 역함수 계산
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    
    # 히스토그램 평활화 적용
    equalized_image = cdf[gray_image]
    
    return equalized_image




#my function
img=cv.imread("../source/pooh.jpg")
start=time.time()
myEqualizeHist(img)
print("MyFunc time:",time.time()-start)

#openCV function
img2=cv.imread("../sourcr/pooh.jpg",cv.IMREAD_GRAYSCALE)
start=time.time()
cv.equalizeHist(img2)
print("OpenCV time:",time.time()-start)

