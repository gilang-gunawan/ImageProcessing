import cv2
import numpy as np

## RGB to CSV ##

def RGBtoHSV(image):
    row, col, ch = image.shape
    #bikin kanvas kosong dengan 3 elemen
    kanvas = np.zeros((row, col, 3), np.uint8)

    for i in range(0, row):
        for j in range(0, col):
            blue, green, red = image[i, j]
            blue = float(blue)
            green = float(green)
            red = float(red)
            maks = max(blue, green, red)
            mins = min(blue, green, red)

            #ngitung v
            v = maks

            #ngitung s
            if(v != 0):
                s = (v - mins)/v
            else:
                s = 0

            #ngitung h
            if(v == mins):
                h = 360
            elif(v == red):
                h = 60*(green - blue)/(v - mins)
            elif(v == green):
                h = 120 + 60*(blue - red)/(v - mins)
            elif(v == blue):
                h = 240 + 60*(red - green)/(v - mins)

            #convert hasil hsv ke angka rgb untuk ditampilkan di layar, kecuali v, karena v=red atau green atau blue (sudah rgb)
            s = s*255
            #print(s)
            h = h/2
            #print(h)

            #assignment ke kanvas baru masing2 elemennya (0 for h, 1 for s, 2 for v)
            kanvas.itemset((i, j, 0), h)
            kanvas.itemset((i, j, 1), s)
            kanvas.itemset((i, j, 2), v)
    return kanvas

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#HSVtoRGB

def HSVtoRGB(image):
    row, col, ch = image.shape
    #bikin kanvas kosong dengan 3 elemen
    kanvas = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            h, s, v = image[i, j]

            h = h*2
            s = s/255
            v = v/255

            c = v * s
            x = c * (1 - abs(((h/60) % 2) -1))
            m = v - c

            r, g, b = 0, 0, 0
            #hitung rgb
            if(h>=0 and h<60):
                r, g, b = c, x, 0
            elif(h>=60 and h<120):
                r, g, b = x, c, 0
            elif(h>=120 and h<180):
                r, g, b = 0, c, x
            elif(h>=180 and h<240):
                r, g, b = 0, x, c
            elif(h>=240 and h<300):
                r, g, b = x, 0, c
            elif(h>=300 and h<360):
                r, g, b = c, 0, x

            r, g, b = (r+m)*255, (g+m)*255, (b+m)*255
            kanvas.itemset((i, j, 0), b)
            kanvas.itemset((i, j, 1), g)
            kanvas.itemset((i, j, 2), r)
    return kanvas

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
##FACE DETECTION

# #Fungsi konvolusi dengan 2 parameter, yaitu image sebagai representasi citra inputan dan mask sebagai filter yang digunakan

def faceDetection(image):
    row, col, ch = image.shape
    kanvas = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0, col):

            intensitas = image[i, j]
            if(intensitas[0] > 19 and intensitas[0] < 240): #nilai 19<H<240 berdasarkan artikel yg terlampir di dalam folder, katanya: kalau lebih atau kurang dari angka2 itu -> bukan kulit manusia
                intensitas[0] = 0
                intensitas[1] = 0
                intensitas[2] = 0
            kanvas.itemset((i, j, 0), int(intensitas[0]))
            kanvas.itemset((i, j, 1), int(intensitas[1]))
            kanvas.itemset((i, j, 2), int(intensitas[2]))
    return kanvas

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## MAIN ##

face = cv2.imread("FACE DETECTION.png")
cv2.imshow("aseli", face)

hsvFace = RGBtoHSV(face)
cv2.imshow("RGBtoHSV", hsvFace)

faceDetect = faceDetection(hsvFace)
cv2.imshow("Deteksi Wajah - HSV", faceDetect)

hasil = HSVtoRGB(faceDetect)
cv2.imshow("Deteksi Wajah - HSVtoRGB", hasil)

cv2.waitKey()
cv2.destroyAllWindows()
