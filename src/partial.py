import cv2
import numpy as np
import sys
original = cv2.imread(sys.argv[1])
image_to_compare = cv2.imread(sys.argv[2])
# 1) Check if 2 images are equals
if original.shape == image_to_compare.shape:
    print("The images have same size and channels")
    difference = cv2.subtract(original, image_to_compare)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("The images are NOT equal")
# 2) Check for similarities between the 2 images
# sift = cv2.xfeatures2d.SIFT_create()

star = cv2.xfeatures2d.StarDetector_create()

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
kp_1 = star.detect(original, None)
kp_2 = star.detect(image_to_compare, None)

kp_1, desc_1 = brief.compute(original, kp_1)
kp_2, desc_2 = brief.compute(original, kp_2)

index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

desc_1 = np.float32(desc_1)
desc_2 = np.float32(desc_2)

matches = flann.knnMatch(desc_1, desc_2, k=2)
good_points = []
for m, n in matches:
    if m.distance < 0.6*n.distance:
        good_points.append(m)
# Define how similar they are
number_keypoints = 0
if len(kp_1) >= len(kp_2):
    number_keypoints = len(kp_1)
else:
    number_keypoints = len(kp_2)

print("Keypoints 1ST Image: " + str(len(kp_1)))
print("Keypoints 2ND Image: " + str(len(kp_2)))
print("GOOD Matches:", len(good_points))
print("How good it's the match: ", len(good_points) / number_keypoints * 100)

result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)

cv2.imshow("result", cv2.resize(result, None, fx=0.4, fy=0.4))
cv2.imwrite("feature_matching.jpg", result)
# cv2.imshow("Original", cv2.resize(original, None, fx=0.4, fy=0.4))
# cv2.imshow("Duplicate", cv2.resize(image_to_compare, None, fx=0.4, fy=0.4))
cv2.waitKey(0)
cv2.destroyAllWindows()
