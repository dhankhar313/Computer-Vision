import cv2
from matplotlib import pyplot as plt
import numpy as np


def course2(fname, height, width):
    img = cv2.imread(fname)
    img = cv2.resize(img, (height, width))
    # cv2.imshow("Hy", img)
    # cv2.waitKey(0)


course2('E:\\1.jpg', 1840, 1440)
