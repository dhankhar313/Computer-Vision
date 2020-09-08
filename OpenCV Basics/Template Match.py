import cv2
import numpy as np

img = cv2.imread('data\\stuff.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
temp = cv2.imread('data\\Capture.PNG', 0)
h, w = temp.shape

final = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED)
point = 0.934
high = np.where(final >= point)
# print(high)

for i in zip(*high[::-1]):
    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 255, 0), 2)

cv2.imshow('Img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
