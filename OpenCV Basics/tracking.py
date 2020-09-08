import cv2
import numpy as np

vid = cv2.VideoCapture(0)
cv2.namedWindow("Feed")


def free(x):
    pass


cv2.createTrackbar("lower_hue0", "Feed", 0, 255, free)
cv2.createTrackbar("lower_sat0", "Feed", 0, 255, free)
cv2.createTrackbar("lower_value0", "Feed", 0, 255, free)
cv2.createTrackbar("upper_hue0", "Feed", 0, 255, free)
cv2.createTrackbar("upper_sat0", "Feed", 0, 255, free)
cv2.createTrackbar("upper_value0", "Feed", 0, 255, free)

while True:
    frame = vid.read()[-1]
    # frame = cv2.imread('data\smarties.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_hue = cv2.getTrackbarPos("lower_hue0", "Feed")
    lower_sat = cv2.getTrackbarPos("lower_sat0", "Feed")
    lower_value = cv2.getTrackbarPos("lower_value0", "Feed")
    upper_hue = cv2.getTrackbarPos("upper_hue0", "Feed")
    upper_sat = cv2.getTrackbarPos("upper_sat0", "Feed")
    upper_value = cv2.getTrackbarPos("upper_value0", "Feed")

    lower_range = np.array([lower_hue, lower_sat, lower_value])
    upper_range = np.array([upper_hue, upper_sat, upper_value])

    mask = cv2.inRange(hsv, lower_range, upper_range)

    final = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Final", final)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
vid.release()
