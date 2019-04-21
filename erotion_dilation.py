import cv2
import numpy as np

def treshold(img):
    row, col = img.shape
    treshold = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            val = img[i, j]
            if (val <= 127):
                val = 0
            if (val > 127):
                val = 255

            treshold.itemset((i, j, 0), val)
    return treshold

def tresneg(img):
    row,col,ch = img.shape
    thres = np.zeros((row,col,1), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            val = img[i,j]
            if val == 0:
                val =255
            else:
                val = 0
            thres.itemset((i,j,0),val)
    return thres

def subrgbgray(rgb, treshold):
    row, col, raw = rgb.shape
    output = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            if treshold[i, j] != 255:
                output.itemset((i, j, 0), 0)
                output.itemset((i, j, 1), 0)
                output.itemset((i, j, 2), 0)
            else:
                output[i, j] = rgb[i, j]
    return output


def ero(img, kernel):
    row, col, _ = img.shape
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            hasil = 0

            if (i - kernel // 2 < 0) or (i + kernel // 2 > row - 1) or (j - kernel // 2) < 0 or (
                    j + kernel // 2 > col - 1):
                continue
            for ii in range(i - kernel // 2, i + kernel // 2 + 1):
                for jj in range(j - kernel // 2, j + kernel // 2 + 1):
                    if img[ii][jj] > 0:
                        hasil += 1
            if (hasil == kernel * kernel):
                canvas.itemset((i, j, 0), 255)
    return canvas


def dil(img, kernel):
    row, col, _ = img.shape
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            hasil = 0

            if (i - kernel // 2 < 0) or (i + kernel // 2 > row - 1) or (j - kernel // 2) < 0 or (
                    j + kernel // 2 > col - 1):
                continue
            for ii in range(i - kernel // 2, i + kernel // 2 + 1):
                for jj in range(j - kernel // 2, j + kernel // 2 + 1):
                    if img[ii][jj] > 0:
                        hasil += 1
            if (hasil > 0):
                canvas.itemset((i, j, 0), 255)
    return canvas

img = cv2.imread('tomat-single.jpg')
row,col,ch= img.shape
b,g,r = cv2.split(img)
b = treshold(r)
# b = tresneg(b)
cv2.imshow("img",img)
cv2.imshow("r",r)
cv2.imshow("g",g)
cv2.imshow("b",b)

b=dil(b,5)
b=ero(b,5)

cv2.imshow("closing", b)

b = subrgbgray(img,b)
cv2.imshow("hasil", b)

# noise = cv2.imread('tomat-single.jpg',0)
# noise_biner = treshold(noise)

# cv2.imshow("biner", noise_biner)


cv2.waitKey(0)
