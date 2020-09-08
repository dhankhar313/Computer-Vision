import cv2


def resize(fname, height, width):
    image = cv2.imread(fname)
    cv2.imshow("Img", image)
    cv2.waitKey(0)
    h, w = image.shape[0:2]
    print(h, w)
    img = cv2.resize(image, (height, width))
    cv2.imshow("Modified", img)
    cv2.waitKey(0)


resize("E:\\1.jpg", 1280, 1280)
cv2.waitKey(0)