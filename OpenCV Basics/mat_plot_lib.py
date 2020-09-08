import matplotlib.pyplot as plt
import cv2

img = cv2.imread('data\sudoku.png', 0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
tf, demo0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
demo1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
demo2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
names = ['No th', 'Normal th', 'Adaptive th 1', 'Adaptive th 2']
pics = [img, demo0, demo1, demo2]
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(pics[i], 'gray')
    plt.title(names[i])
    plt.xticks([]), plt.yticks([])

plt.show()
