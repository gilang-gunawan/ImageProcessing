import cv2
import numpy as np

img = cv2.imread("Lenna.png",0)

dx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(img, cv2.CV_32F, 0, 1)

abs_dx = cv2.convertScaleAbs(dx)
abs_dy = cv2.convertScaleAbs(dy)

cv2.imshow("sobel x", abs_dx)
cv2.imshow("sobel y", abs_dy)

cv2.waitKey(0)
cv2.destroyAllWindows()