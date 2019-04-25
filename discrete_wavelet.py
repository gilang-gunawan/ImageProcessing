import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt

img = cv2.imread('Apel-Merah.jpg',0)

coef = pywt.dwt2(img, 'db4')
ll, (lh, hl, hh) = coef

fig, ax = plt.subplots(2,2, figsize=(20,20))
ax[0,0].imshow(ll, cmap='gray')
ax[0,1].imshow(lh, cmap='gray')
ax[1,0].imshow(hl, cmap='gray')
ax[1,1].imshow(hh, cmap='gray')

coef2 = pywt.dwt2(ll, 'db4')
ll, (lh, hl, hh) = coef2

fig, ax = plt.subplots(2,2, figsize=(20,20))
ax[0,0].imshow(ll, cmap='gray')
ax[0,1].imshow(lh, cmap='gray')
ax[1,0].imshow(hl, cmap='gray')
ax[1,1].imshow(hh, cmap='gray')

plt.show()
