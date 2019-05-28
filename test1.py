import numpy as np
#pip install opencv_python 安裝OPENCV
from cv2 import cv2
#pip install  imutils 安裝輪廓
import imutils
def displayIMG(img, windowName):

    cv2.namedWindow( windowName, cv2.WINDOW_NORMAL )

    cv2.resizeWindow(windowName, 1000, 800)

    cv2.imshow(windowName, img)

    #htitch= np.hstack((img1, img3,img4))  合併圖片
    
image = cv2.imread('D:\\PYTHON_TEST\\images\\TEST1.PNG',cv2.COLOR_BGR2GRAY)
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)

sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))

sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

displayIMG(sobelX, "SibelX")

displayIMG(sobelY, "SibelY")

displayIMG(sobelCombined, "SibelXY")

canny = cv2.Canny(image, 30, 150)

displayIMG(canny, "Canny")


cv2.waitKey(0)
cv2.destroyAllWindows()
