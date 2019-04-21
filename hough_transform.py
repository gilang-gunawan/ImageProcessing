#HOUGH
import cv2
import numpy as np
import math as m

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

def konvolusi(img,kernel):
    row,col=img.shape
    mrow,mcol=kernel.shape
    h=int(mrow/2)

    canvas=np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if i==0 or i==row-1 or j==0 or j==col-1:
                canvas.itemset((i,j),0)
            else:
                sums=0
                for a in range(-h,mrow-h):
                    for b in range(-h,mcol-h):
                        temp=img[i+a,j+b]*kernel[h+a,h+b]
                        sums+=temp
                canvas.itemset((i,j),sums)
    return canvas

def edgedetection(img):
    kernel=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],np.float32)
    ker=kernel/8
    canvas=konvolusi(img,ker)
    return canvas

def findcoordinates(img):
    coor = []
    row,col=img.shape
    for i in range(0,row):
        for j in range(0,col):
            if img[i,j]==255:
                coor.append([i,j])
    return coor

def hough(koordinat,sudut,threshold):
    k=len(koordinat)
    s=len(sudut)
    r=np.zeros((k,s))
    for i in range(k):
        for j in range(s):
            hasil=(koordinat[i][0]*m.cos(m.pi*sudut[j]))+(koordinat[i][1]*m.sin(m.pi*sudut[j]))
            r.itemset((i,j),round(hasil,1))
    nilai_r=np.unique(r)
    lenr=len(nilai_r)
    result = np.where(r[:,0] == -142)
    frekuensi=np.zeros((s,len(nilai_r)))
    for i in range(s):
        for j in range(lenr):
            idx=np.where(r[:,i] == nilai_r[j])
            frekuensi.itemset((i,j), len(idx[0]))
    rowf,colf=frekuensi.shape
    rtheta=[]
    for i in range(rowf):
        for j in range(colf):
            if frekuensi[i,j]>=threshold:
                rtheta.append([sudut[i],nilai_r[j]])
    return rtheta

img=cv2.imread("sudo.png",0)
img2=cv2.imread("sudo.png")
edge=edgedetection(img)
biner=konversi_ke_biner(edge,100)
cv2.imshow("biner",biner)
sudut=[-0.5,-0.25,0,0.25,0.5]
find_coor =findcoordinates(biner)
print(find_coor)

h=hough(find_coor,sudut,100)
print(h)
for i in range(len(h)):
        theta,rho = h[i]
        b = m.cos(theta*m.pi)
        a = m.sin(theta*m.pi)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img2,(x1,y1),(x2,y2),(255,0,255),2)


# cv2.imshow("Hasil", edge)
cv2.imshow("hasil", img2)
cv2.waitKey()
cv2.destroyAllWindows()