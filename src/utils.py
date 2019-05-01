"""
Util functions
"""
from cv2 import imread
from config import ROLL

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

def best_image(frames, slides) -> list:
    """
    Get the ppt matches
    """
    ret = []
    for frame in frames:
        for slide in slides:
            # do shiz
            ret.append("Highest match")
    return ret
