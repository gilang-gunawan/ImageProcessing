##REGIONFILL
import cv2
import numpy as np

def konversi_ke_biner(img, thres):
    row,col=img.shape
    binary=np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if img[i,j] > thres:
                binary.itemset((i,j),255)
            else:
                binary.itemset((i,j),0)
    return binary

def invers(img):
    row,col=img.shape
    canvas=np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if img[i,j]==255:
                canvas.itemset((i,j),0)
            else:
                canvas.itemset((i,j),255)
    return canvas

def union(img, dil):
    row,col=img.shape
    canvas=np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            temp=int(img[i,j] | dil[i,j])
            canvas.itemset((i,j),temp)
    return canvas

def intersect(img, dil):
    row,col=img.shape
    canvas=np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            temp=int(img[i,j] & dil[i,j])
            canvas.itemset((i,j),temp)
    return canvas

def dilasi_per_pixel(img,se,pixeli,pixelj):
    srow,scol=se.shape
    h=int(srow/2)
    temp=0
    for a in range(-h,srow-h):
        for b in range(-h,scol-h):
            if se[h+a,h+b] != 0:
                temp = img[pixeli+a,pixelj+b] & se[h+a,h+b]
                if temp == 1:
                    break
        if temp == 1:
            return 255
    if temp == 0:
        return 0

def fill(img,a,b,warna):
    row,col=img.shape
    bg=img[a,b]
    stack=set(((a ,b),))
    while stack:
        i,j = stack.pop()
        if img[i,j] == bg:
            img[i,j] = warna
            if i > 0:
                stack.add((i-1,j))
            if i < (row-1):
                stack.add((i+1,j))
            if j > 0:
                stack.add((i,j-1))
            if j < (col-1):
                stack.add((i,j+1))

def regionfilling(img,se):
    row,col=img.shape
    canvas=np.zeros((row,col),np.uint8)
    biner=konversi_ke_biner(img,100)
    cv2.imshow("citra biner",biner)
#mencari lubang
    lubang=konversi_ke_biner(img,100)
    fill(lubang,0,0,100)
    cv2.imshow("lubang",lubang)
#melakukan dilasi
    for i in range(0,row):
        for j in range(0,col):
            if lubang[i,j]==0:
                pixel=dilasi_per_pixel(biner,se,i,j)
                canvas.itemset((i,j),pixel)
                biner.itemset((i,j),pixel)
    inver=invers(biner)
    cv2.imshow("canvas",canvas)
    cv2.imshow("biner",biner)
    irisan = intersect(canvas,inver)
    cv2.imshow("irisan",irisan)
    hasil=union(biner,irisan)
    return hasil

img=cv2.imread("filling.jpg",0)
se = np.array([[0,1,0],[1,1,1],[0,1,0]])
hasil=regionfilling(img,se)
cv2.imshow("Hasil", hasil)
cv2.imshow("Ori", img)
cv2.waitKey()
cv2.destroyAllWindows()

