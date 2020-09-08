import cv2
import numpy as np

apple = cv2.imread('data\Apple.jpg')
orange = cv2.imread('data\orange.jpg')
print(apple.shape)
print(orange.shape)
rough_merge = np.hstack((apple[:, :256], orange[:, 256:]))
cv2.imshow("Rough Merge", rough_merge)
cv2.waitKey(3000)

# Gaussian Pyramid for Apple
apple_copy = apple.copy()
gaussian_apple = []
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gaussian_apple.append(apple_copy)

# Gaussian Pyramid for Orange
orange_copy = orange.copy()
gaussian_orange = []
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gaussian_orange.append(orange_copy)

# Laplacian Pyramid for Apple
apple_copy = gp_apple[-1]
laplacian_apple = [apple_copy]
for i in range(5,0,-1):
    
