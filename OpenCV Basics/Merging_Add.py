import cv2
import numpy as np

img = cv2.imread('data\lena.jpg')
img2 = cv2.imread('data\fruits.jpg')
r, c, d = img.shape
print(r, c, d)
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
img2 = cv2.resize(img2, (512, 512))
eye = img[280:340, 330:390]
img[273:333, 100:160] = eye
# hybrid = cv2.add(img, img2)
hybrid = cv2.addWeighted(img, 0.5, img2, 0.5, 0)
cv2.imshow("Added", hybrid)
cv2.waitKey(0)
