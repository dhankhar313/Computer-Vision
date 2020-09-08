import cv2
import numpy as np

# img = cv2.imread('data\lena.jpg', 1)
img = np.zeros([1024, 1024, 3])
cv2.rectangle(img, (50, 50), (500, 500), (255, 0, 0), -1)
cv2.circle(img, (250, 250), 100, (0, 0, 255), -1)
cv2.putText(img, 'Hello', (400, 750), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 3)
cv2.imshow('Lena', img)
cv2.waitKey(2000)
