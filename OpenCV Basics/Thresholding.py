import cv2

img = cv2.imread('data\sudoku.png', 0)
# Normal Thresholding
tf, demo0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Adaptive Thresholding
demo1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
demo2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 2)

cv2.imshow("Img", img)
cv2.imshow("Normal", demo0)
cv2.imshow("Adaptive Mean", demo1)
cv2.imshow("Adaptive Gaussian", demo2)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
