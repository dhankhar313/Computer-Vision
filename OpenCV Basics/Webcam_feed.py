import cv2
import datetime

vid = cv2.VideoCapture(0)
four_cc = cv2.VideoWriter_fourcc(*'XVID')
op = cv2.VideoWriter("Webcam Feed.mkv", four_cc, 30.0, (640, 480))
vid.set(4, 720)
vid.set(3, 1280)

print(vid.get(4))
while vid.isOpened():
    frame = vid.read()[-1]
    data = 'Height:' + str(vid.get(4))
    data2 = 'Width:' + str(vid.get(3))
    date = str(datetime.datetime.now())
    frame = cv2.putText(frame, data, (10, 15),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
    frame = cv2.putText(frame, data2, (10, 35),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
    frame = cv2.putText(frame, date, (1000, 710),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
    # op.write(frame)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Feed", frame)
    if cv2.waitKey(1) == ord("g"):
        break
vid.release()
op.release()
cv2.destroyAllWindows()
