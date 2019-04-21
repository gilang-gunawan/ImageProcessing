import numpy as np
import cv2


def konversi_ke_biner(img1): #konversi ke citra biner
    row, col = img1.shape
    konversi = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            val = img1[i, j]
            if (val <= 55):
                val = 0
            if (val > 55):
                val = 255
            konversi.itemset((i, j, 0), val)
    return konversi

def biner_tomat(img):
    row, col, ch = img.shape
    konversi = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            val = img[i, j]
            if (val <= 55):
                val = 0
            if (val > 55):
                val = 255
            konversi.itemset((i, j, 0), val)
    return konversi

def substract(image, image2):
    row, col = image.shape
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            subs = int(image[i, j]) - int(image2[i, j])
            if (subs < 0):
                canvas.itemset((i, j, 0), 0)
            else:
                canvas.itemset((i, j, 0), subs)
    return canvas


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

def erosi(img, kernel):
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

def dilasi(img, kernel):
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


## NO 1 - Citra Noise
#konversi ke biner
noise = cv2.imread('noise.jpg',0)
noise_biner = konversi_ke_biner(noise)
cv2.imshow("noise biner", noise_biner)

#erosi
noise_erosi = erosi(noise_biner,5) #kernel 5x5
cv2.imshow("hasil erosi", noise_erosi)

##NO 2 - Opening
img_opening = cv2.imread('opening.jpg',0)
hasil_biner = konversi_ke_biner(img_opening)

cv2.imshow("opening biner", hasil_biner)

#erosi
img_erosi = erosi(hasil_biner,7)
#dilasi
img_opening = dilasi(img_erosi, 7)

cv2.imshow("img after opening", img_opening)

##NO 3 - Closing
img_closing = cv2.imread('closing.jpg',0)
hasil_biner = konversi_ke_biner(img_closing)

cv2.imshow("closing biner", hasil_biner)

#dilasi
img_dilasi = dilasi(hasil_biner,13)
#erosi
img_closing = erosi(img_dilasi,7)

cv2.imshow("img after closing", img_closing)

##NO 4 - tomat
tomat = cv2.imread('tomat-single.jpg')
b, g, r = cv2.split(tomat)
b = biner_tomat(substract(r, g))
cv2.imshow("tomat biner", b)

#closing
b = dilasi(b,7)
b = erosi(b,5)
cv2.imshow("tomat closing", b)

#ubah ke bentuk RGB
b = subrgbgray(tomat, b)
cv2.imshow("hasil akhir", b)

cv2.waitKey(0)
cv2.destroyAllWindows()