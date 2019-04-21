import cv2
import numpy as np

img = cv2.imread("original.jpg",0)

tr, th = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

cv2.imshow('original', th)
#
se = np.ones((5,5), np.uint8)

# erosi
erosi = cv2.erode(th, se, iterations=2)
cv2.imshow('erosi', erosi)

#dilasi
dilasi = cv2.dilate(th, se, iterations=2)
cv2.imshow('dilasi', dilasi)

#opening

img2 = cv2.imread("opening.jpg",0)
tr2, th2 = cv2.threshold(img2, 128, 255, cv2.THRESH_BINARY)

#cara 1
res = cv2.erode(th2, se, iterations=5)
res = cv2.dilate(res, se, iterations=5)

#cara 2
res = cv2.morphologyEx(th2, cv2.MORPH_OPEN, se, iterations=5)
#
cv2.imshow('opening', img2)
cv2.imshow('hasil opening', res)

#closing
img2 = cv2.imread("closing.jpg",0)
tr2, th2 = cv2.threshold(img2, 128, 255, cv2.THRESH_BINARY)

res = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, se, iterations=5)

cv2.imshow('closing', img2)
cv2.imshow('hasil closing', res)


cv2.waitKey()
cv2.destroyAllWindows()