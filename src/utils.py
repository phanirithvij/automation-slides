"""
Util functions
"""
import cv2
from config import ROLL

def touch_file(filename="{}.txt".format(ROLL)):
    """
    Touches output file
    """
    with open(filename, "w+") as _out:
        pass

def imread(image=""):
    """
    Read image
    """
    return cv2.imread(image)

def best_image(frames, slides) -> list:
    """
    Get the ppt matches
    """
    ret = []
    # sift = cv2.xfeature2d.SIFT_create()
    frs = [imread(im) for im in frames]
    slds = [imread(im) for im in slides]
    for idx, frame in enumerate(frames):
        maxed  = 0
        cslide = ""
        for jdx, slide in enumerate(slides):
            frm  = frs[idx]
            slid = slds[jdx]

            # keypoints, desc1 = sift.detectAndCompute(frm, )

            # percent =
            # if maxed <
            pass
        ret.append({
            "percent"       : maxed,
            "slide"         : cslide,
            "frame"         : frame
        })
    return ret
