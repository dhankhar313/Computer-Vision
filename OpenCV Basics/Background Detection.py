import cv2
import matplotlib.pyplot as plt

vid = cv2.VideoCapture('data\\vtest.avi')
fgbg1 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
fgbg2 = cv2.createBackgroundSubtractorKNN(detectShadows=True)

while vid.isOpened():
    frame = vid.read()[-1]

    mask1 = fgbg1.apply(frame)
    mask2 = fgbg2.apply(frame)

    names = ['Default', 'MOG2', 'KNN']
    frames = [frame, mask1, mask2]

    # KNN has much less Noise

    cv2.imshow('Default', frame)
    cv2.imshow('MOG2', mask1)
    cv2.imshow('KNN', mask2)

    # for i in range(3):
    #     plt.subplot(1, 3, i + 1)
    #     plt.imshow(frames[i], 'gray')
    #     plt.title(names[i])
    #     plt.xticks([])
    #     plt.yticks([])
    if cv2.waitKey(30) == 27:
        break

# plt.show()
cv2.destroyAllWindows()
