"""
Convert the given dataset to a required format
"""
import os
from shutil import copy

DEST = "Data"
SRC = os.path.abspath("../Data/Dataset")
SLIDES = os.path.join(DEST, "slides")
FRAMES = os.path.join(DEST, "frames")

try:
    os.makedirs(DEST)
except FileExistsError:
    print("Directory exists")
    try:
        os.makedirs(SLIDES)
        os.makedirs(FRAMES)
    except FileExistsError:
        print("file exists")

for dire in os.listdir(SRC):
    direa = os.path.abspath(os.path.join("../Data/Dataset", dire))
    for x in os.listdir(direa):
        xa = os.path.abspath(os.path.join("../Data/Dataset", direa, x))
        if "ppt" in x:
            newname = os.path.abspath(os.path.join(SLIDES, dire + "_" + x))
            copy(xa, newname)
            print(xa, newname)

        else:
            newname = os.path.abspath(os.path.join(FRAMES, dire + "_" + x))
            copy(xa, newname)
            print(xa, newname)
