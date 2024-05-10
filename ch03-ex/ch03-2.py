import cv2 as cv
import matplotlib.pyplot as plt


img=cv.imread("../source/pooh.jpg")

if img is None:
    print("no file")

h=cv.calcHist([img],[2],None,[256],[0,256])
plt.plot(h,color='r',linewidth=1)

