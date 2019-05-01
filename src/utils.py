"""
Util functions
"""
from config import ROLL
from cv2 import imread

def touch_file(filename="{}.txt".format(ROLL)):
    """
    Touches output file
    """
    with open(filename, "w+") as _out:
        pass

def imread_c(image=""):
    """
    Read image
    """
    return imread(image)