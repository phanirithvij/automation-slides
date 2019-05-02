"""
Util functions
"""
import os
import time
import cv2
from matplotlib import pyplot as plt
from config import ROLL


def touch_file(filename="{}.txt".format(ROLL)):
    """
    Touches output file
    """
    with open(filename, "w+") as _out:
        pass

def write_file(content, filename="{}.txt".format(ROLL)):
    """
    Write content
    """
    with open(filename, "w+") as file:
        file.write(content)


def imread(image=""):
    """
    Read image
    """
    return cv2.imread(image)

def best_images(frames, slides) -> list:
    """
    Get the ppt matches
    """
    # sift = cv2.ORB_create()
    sift = cv2.xfeatures2d.SIFT_create()

    ret = []
    keyframes = []
    keyslides = []
    FLANN_INDEX_LSH = 0
    # FLANN_INDEX_LSH = 6

    index_params = dict(
        algorithm=FLANN_INDEX_LSH,
        # table_number=6, # 12
        # key_size=12,     # 20
        trees=5)
        # multi_probe_level=1) #2
    search_params = dict()
    # search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    start = time.time()
    frs = [imread(im) for im in frames]
    slds = [imread(im) for im in slides]
    print("Took", time.time() - start, "secs")

    # frs = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in frames]
    # slds = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in slides]

    for f_r in frs:
        keypoints, descriptors = sift.detectAndCompute(f_r, None)
        keyframes.append((keypoints, descriptors))
    for s_l in slds:
        keypoints, descriptors = sift.detectAndCompute(s_l, None)
        keyslides.append((keypoints, descriptors))

    for idx, frame in enumerate(frames):
        max_percent = 0
        cslide = slides[0]
        for jdx, slide in enumerate(slides):
            # frm = frs[idx]
            # slid = slds[jdx]
            kp1, ds1 = keyframes[idx]
            kp2, ds2 = keyslides[jdx]

            matches = flann.knnMatch(ds1, ds2, k=2)
            # print(matches)

            good_points = []
            for x_snake in matches:
                # try:
                m_snake = x_snake[0]
                n_snake = x_snake[1]
                # except IndexError:
                    # print("dead")
                    # pass
                if m_snake.distance < 0.6*n_snake.distance:
                    good_points.append(m_snake)

            number_keypoints = 0
            if len(kp1) >= len(kp2):
                number_keypoints = len(kp1)
            else:
                number_keypoints = len(kp2)
            print("num points", len(kp1), len(kp2))

            percent = len(good_points) / number_keypoints * 100
            # percent = 0

            if max_percent < percent:
                max_percent = percent
                cslide = slide

        cslide = cslide.split("\\")[-1]
        frame = frame.split("\\")[-1]
        ret.append([cslide, frame, percent])
    return ret
