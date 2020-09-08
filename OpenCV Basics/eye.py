    import cv2

    video = cv2.VideoCapture(0)

    ''' The xml file can be found in the opencv repository on github under "opencv-master\data\haarcascades" '''
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

    frame = video.read()[-1]
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eye = eye_cascade.detectMultiScale(gray_frame)

    if len(eye) == 0:
        print("Eyes closed or not detected")
    else:
        for (x1, y1, w1, h1) in eye:
            cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)

            cv2.imshow('Eye Detection', frame)

            if cv2.waitKey(0) == 27:
                break

    video.release()
    cv2.destroyAllWindows()
