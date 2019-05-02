"""
Util functions
"""
# import os
import time
import cv2
import numpy as np
# from matplotlib import pyplot as plt
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
    # sift = cv2.xfeatures2d.SIFT_create()
    # Initiate STAR detector
    # star = cv2.FeatureDetector_create("STAR")
    star = cv2.xfeatures2d.StarDetector_create()

    # Initiate BRIEF extractor
    # brief = cv2.DescriptorExtractor_create("BRIEF")
    brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

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
    frs = [cv2.imread(im, 0) for im in frames]
    slds = [cv2.imread(im, 0) for im in slides]
    print("Took", time.time() - start, "secs to read images")

    # frs = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in frames]
    # slds = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in slides]

    prev_t = time.time()
    for f_r in frs:
        # keypoints, descriptors = sift.detectAndCompute(f_r, None)
        keypoints = star.detect(f_r, None)
        keypoints, descriptors = brief.compute(f_r, keypoints)
        keyframes.append((keypoints, descriptors))
        print("Took", time.time() - prev_t, "secs to read")
        prev_t = time.time()
    for s_l in slds:
        # keypoints, descriptors = sift.detectAndCompute(s_l, None)
        keypoints = star.detect(s_l, None)
        keypoints, descriptors = brief.compute(s_l, keypoints)
        keyslides.append((keypoints, descriptors))
        print("Took", time.time() - prev_t, "secs to read")
        prev_t = time.time()

    for idx, frame in enumerate(frames):
        max_percent = 0
        cslide = slides[0]
        for jdx, slide in enumerate(slides):
            kp1, ds1 = keyframes[idx]
            kp2, ds2 = keyslides[jdx]

            ds1 = np.float32(ds1)
            ds2 = np.float32(ds2)
            # ds2 = ds2.astype(int)

            matches = flann.knnMatch(ds1, ds2, k=2)
            # print("matches++")

            good_points = []
            for x_snake in matches:
                m_snake = x_snake[0]
                n_snake = x_snake[1]
                if m_snake.distance < 0.6*n_snake.distance:
                    good_points.append(m_snake)

            number_keypoints = 0
            if len(kp1) >= len(kp2):
                number_keypoints = len(kp1)
            else:
                number_keypoints = len(kp2)
            # print("Filenames", frame, slide)
            # print("key 1", len(kp1))
            # print("key 2", len(kp2))
            # print("num good points", len(good_points))
            # print("num keypoints", number_keypoints)

            percent = len(good_points) / number_keypoints * 100
            # percent = 0

            if max_percent < percent:
                max_percent = percent
                cslide = slide

        cslide = cslide.split("\\")[-1]
        frame = frame.split("\\")[-1]
        ret.append([cslide, frame, percent])
        print(f"{frame} {cslide} {percent}")
    return ret
