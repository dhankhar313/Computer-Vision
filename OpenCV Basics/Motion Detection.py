import cv2

video = cv2.VideoCapture('data\\vtest.avi')

frame1 = video.read()[-1]
frame2 = video.read()[-1]

while video.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    threshold = cv2.threshold(blurred, 20, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)[-1]
    morphed = cv2.morphologyEx(threshold, cv2.MORPH_CROSS, None)
    contours = cv2.findContours(morphed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

    for arr in contours:
        x, y, w, h = cv2.boundingRect(arr)
        if cv2.contourArea(arr) < 350:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Movement Detected", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),
                    2)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow('Video', frame1)

    frame1 = frame2
    frame2 = video.read()[-1]

    if cv2.waitKey(70) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
