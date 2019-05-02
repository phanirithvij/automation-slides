#!/usr/bin/env python3
"""
main file
"""
import sys
import os
from config import ROLL
from conf import USAGE_MESSAGE
from utils import touch_file, best_images, write_file

def init_packages():
    """
    Download requirements
    """
    print("Downloading python packages")
    os.system("python -m pip install -r requirements.txt")
    # try:
    #     os.system("python -m pip install -r src\\requirements.txt")
    # except Exception:
    #     pass

if __name__ == "__main__":
    init_packages()
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

    slider = []
    framer = []

    for slide in slides:
        slider.append(os.path.abspath(os.path.join(PATH_SLIDES, slide)))
    for frame in frames:
        framer.append(os.path.abspath(os.path.join(PATH_FRAMES, frame)))

    # print(framer)
    data = best_images(framer, slider)

    content = ""
    for datum in data:
        content += f"{datum[1]} {datum[0]}\n"
    write_file(content)

    # imag = os.path.abspath(os.path.join("..", "Data", "Dataset", "02_0", "0.jpg"))
    # if os.path.exists(imag):
    #     IMAGE = cv2.imread(imag)
    #     cv2.imshow("bruh", IMAGE)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    # else:
    #     print("Image doesn't exist", imag)

    print(f"{sys.argv[0]} {PATH_SLIDES} {PATH_FRAMES}")
