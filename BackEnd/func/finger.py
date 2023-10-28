import cv2

def compare_fingerprints(uploaded_keypoints, uploaded_descriptors, stored_keypoints, stored_descriptors):
    keypoints_1 = uploaded_keypoints
    descriptors_1 = uploaded_descriptors
    keypoints_2 = stored_keypoints
    descriptors_2 = stored_descriptors

    matches = cv2.FlannBasedMatcher({"algorithm": 1, "trees": 10}, {}).knnMatch(descriptors_1, descriptors_2, k=2)
    match_points = []

    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            match_points.append(p)
    keypoints_count = min(len(keypoints_1), len(keypoints_2))
    match_score = len(match_points) / keypoints_count * 100

    return match_score
