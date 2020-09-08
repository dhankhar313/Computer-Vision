import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data\smarties.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5)) / 25
filter_2d = cv2.filter2D(img, -1, kernel)
blurred = cv2.blur(img, (5, 5))
Gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
median_blur = cv2.medianBlur(img, 5)
bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)

name = ['Original', '2D Convolution', 'Blurred', 'Gaussian Blur',
        'Median Blur', 'Bilateral Filter']
pics = [img, filter_2d, blurred, Gaussian_blur, median_blur, bilateral_filter]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(pics[i], 'gray')
    plt.title(name[i])
    plt.xticks([]), plt.yticks([])

plt.show()
