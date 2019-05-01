#!/usr/bin/env python3
"""
main file
"""
import sys
import os
import numpy as np
import cv2
from config import ROLL
from conf import USAGE_MESSAGE
from utils import touch_file, best_image

if __name__ == "__main__":
    touch_file()

    if len(sys.argv) < 3:
        print(USAGE_MESSAGE.format(ROLL))
        exit(-1)

    PATH_SLIDES = sys.argv[1]
    PATH_FRAMES = sys.argv[2]
    PATH_FRAMES = os.path.abspath(PATH_FRAMES)
    PATH_SLIDES = os.path.abspath(PATH_SLIDES)

    SLIDES = os.listdir(PATH_SLIDES)
    FRAMES = os.listdir(PATH_FRAMES)

    best_image(FRAMES, SLIDES)

    imag = os.path.abspath(os.path.join("..", "Data", "Dataset", "02_0", "0.jpg"))
    if os.path.exists(imag):
        IMAGE = cv2.imread(imag)
        cv2.imshow("bruh", IMAGE)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image doesn't exist", imag)

    print(f"{sys.argv[0]} {PATH_SLIDES} {PATH_FRAMES}")
