#!/usr/bin/env python3
"""
main file
"""
import sys
import os
import numpy as np
from config import ROLL
from conf import USAGE_MESSAGE
from utils import imread_c, touch_file, best_image

if __name__ == "__main__":
    touch_file()

    if len(sys.argv) < 3:
        print(USAGE_MESSAGE.format(ROLL))
        exit(-1)

    PATH_SLIDES = sys.argv[1]
    PATH_FRAMES = sys.argv[2]
    PATH_FRAMES = os.path.abspath(PATH_FRAMES)
    PATH_SLIDES = os.path.abspath(PATH_SLIDES)

    slides = os.listdir(PATH_SLIDES)
    frames = os.listdir(PATH_FRAMES)

    best_image(frames, slides)

    IMAGE = imread_c(os.path.join("Data", "Dataset", "02_0", "0.jpg"))

    print(f"{sys.argv[0]} {PATH_SLIDES} {PATH_FRAMES}")
