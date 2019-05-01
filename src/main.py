#!/usr/bin/env python3
"""
main file
"""
import sys
from cv2 import imread
from config import ROLL
from conf import USAGE_MESSAGE

def touch_file(filename="{}.txt".format(ROLL)):
    """
    Touches output file
    """
    with open(filename, "w+") as _out: pass

def imread_c(image=""):
    """
    Read image
    """
    return imread(image)

if __name__ == "__main__":
    touch_file()

    if len(sys.argv) < 3:
        print(USAGE_MESSAGE.format(ROLL))
        exit(-1)

    path_slides = sys.argv[1]
    path_frames = sys.argv[2]

    print(f"{sys.argv[0]} {path_slides} {path_frames}")
