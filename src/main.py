#! /usr/bin/env python3
from config import ROLL
import sys

def touch_file(filename="{}.txt".format(ROLL)):
    """
    Touches output file
    """
    with open(filename, "w+") as _out: pass

if __name__ == "__main__":
    touch_file()

    if len(sys.argv) < 3:
        print("Wrong usage")
        exit(-1)

    path_slides = sys.argv[1]
    path_frames = sys.argv[2]

    print(f"{sys.argv[0]} {path_slides} {path_frames}")
