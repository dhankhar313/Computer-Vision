import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data\messi5.jpg', 0)

lap = np.uint8(abs(cv2.Laplacian(img, cv2.CV_64F, ksize=3)))
sobelX = np.uint8(abs(cv2.Sobel(img, cv2.CV_64F, 1, 0)))
sobelY = np.uint8(abs(cv2.Sobel(img, cv2.CV_64F, 0, 1)))

combo = cv2.bitwise_or(sobelX, sobelY)
canny = cv2.Canny(img, 100, 200)

name = ['Img', 'Laplacian', 'Sobel X', 'Sobel Y', 'Combined(Sobel X+Y)', 'Canny']
pics = [img, lap, sobelX, sobelY, combo, canny]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(pics[i], 'gray')
    plt.title(name[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.destroyAllWindows()
