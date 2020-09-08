import cv2
import matplotlib.pyplot as plt
import numpy as np

img0 = cv2.imread('data\\detect_blob.png')
img = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)


# Some images work better with thresholding, some without 
# threshold = cv2.threshold(img, 127, 255, 0)[-1]
contours = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
temp = np.zeros((img0.shape[0], img0.shape[1]))
print(len(contours))
cv2.drawContours(temp, contours, -1, (255, 255, 255), 1)

name = ['Img', 'Gray', 'Contours']
pics = [img0, img, temp]

for i in range(3):
    plt.subplot(2, 2, i + 1)
    plt.imshow(pics[i], 'gray')
    plt.title(name[i])
    plt.xticks([]), plt.yticks([])

plt.show()
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
