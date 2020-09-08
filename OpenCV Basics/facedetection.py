import cv2

video = cv2.VideoCapture('WIN_20200812_21_38_10_Pro.mp4')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

while video.isOpened():
    frame = video.read()[-1]
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray_frame)

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        face_area_gray = gray_frame[y:y + h, x:x + w]
        face_area_color = frame[y:y + h, x:x + w]

        eye = eye_cascade.detectMultiScale(face_area_gray)

        for (x1, y1, w1, h1) in eye:
            cv2.rectangle(face_area_color, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
