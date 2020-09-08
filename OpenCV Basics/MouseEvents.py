import cv2
import numpy as np


def click_command(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img, f"{str(x)}, {str(y)}", (x, y), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)
        cv2.imshow("Coordinates", img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.putText(img, f"{img[x, y, 0]},{img[x, y, 1]},{img[x, y, 2]}",
                    (x, y), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)
        cv2.imshow("Coordinates", img)


img = cv2.imread('data\lena.jpg')
cv2.imshow("Coordinates", img)
cv2.setMouseCallback("Coordinates", click_command)
cv2.waitKey(0)
