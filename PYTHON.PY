
from cv2 import cv2

img = cv2.imread('D:\\PYTHON_TEST\\images\\2998274.jpg',cv2.IMREAD_COLOR)
cv2.imshow('img1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
