import cv2


def blur(image):
    img1 = cv2.imread(image)
    img = cv2.resize(img1, (1280, 1280))
    kernels = [3, 5, 8, 12, 15]
    for i in kernels:
        blurred = cv2.blur(img, ksize=(i, i))
        cv2.imshow(str(i), blurred)
        cv2.waitKey(0)


blur('E:\\IMG_20200112_102018.jpg')
