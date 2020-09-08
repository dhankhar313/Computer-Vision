import cv2
import numpy as np


def sharpen(image):
    img = cv2.imread(image)
    img = cv2.resize(img, (1280, 1280))
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(img, -1, kernel)
    cv2.imshow("Sharp", sharpened)
    cv2.waitKey()


sharpen('E:\\IMG_20200112_102018.jpg')
