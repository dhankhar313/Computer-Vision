import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('data\smarties.png')
colored_mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)[-1]
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_mask = cv2.threshold(img1, 220, 255, cv2.THRESH_BINARY_INV)[-1]

kernel = np.ones((2, 2))
dilation = cv2.morphologyEx(gray_mask, cv2.MORPH_DILATE, kernel)
erosion = cv2.morphologyEx(gray_mask, cv2.MORPH_ERODE, kernel)
# Opening is erosion then dilation
opening = cv2.morphologyEx(gray_mask, cv2.MORPH_OPEN, kernel)
# Closing is Dilation then Erosion
closing = cv2.morphologyEx(gray_mask, cv2.MORPH_CLOSE, kernel)
# Gradient is dilation - erosion
gradient = cv2.morphologyEx(gray_mask, cv2.MORPH_GRADIENT, kernel)
#  tophat is input-opening
tophat = cv2.morphologyEx(gray_mask, cv2.MORPH_TOPHAT, kernel)
cross = cv2.morphologyEx(gray_mask, cv2.MORPH_CROSS, kernel)
ellipse = cv2.morphologyEx(gray_mask, cv2.MORPH_ELLIPSE, kernel)
hitmiss = cv2.morphologyEx(gray_mask, cv2.MORPH_HITMISS, kernel)
rect = cv2.morphologyEx(gray_mask, cv2.MORPH_RECT, kernel)

name = ['Colored', 'Colored_Mask', 'Default_Gray', 'Gray_Mask', 'Dilation', 'Erosion',
        'Opening', 'Closing', 'Gradient', 'TopHat', 'Cross', 'Ellipse', 'Hitmiss', 'Rect']
pics = [img, colored_mask, img1, gray_mask, dilation, erosion,
        opening, closing, gradient, tophat, cross, ellipse, hitmiss, rect]

for i in range(14):
    plt.subplot(4, 4, i + 1)
    plt.imshow(pics[i], 'gray')
    plt.title(name[i])
    plt.xticks([]), plt.yticks([])

plt.show()
