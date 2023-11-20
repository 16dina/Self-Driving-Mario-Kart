import sys
import math
import cv2 as cv
import numpy as np
import matplotlib as plt

img_orig = cv.imread('dataset/b28d0978-96b4-45a6-a0c5-07576afdbb45.png')
img_rgb = cv.cvtColor(img_orig, cv.COLOR_BGR2RGB)

# canny detection without blurring
#img_canny = cv2.Canny(img_rgb, threshold1=321, threshold2=400)
img_canny = cv.Canny(img_rgb, threshold1=280, threshold2=400)
plt.figure(figsize = (15, 15))
plt.subplot(1, 2, 1); plt.imshow(img_rgb)
plt.axis('off')
plt.subplot(1, 2, 2); plt.imshow(img_canny)
plt.axis('off')