import cv2
import numpy as np
import math
from models import haarcascade_frontalface_default
from models import haarcascade_left_eye_2splits

img = cv2.VideoCapture(0)
scaling_factor = 0.7

img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
cv2.imshow('Input', img)
gray = cv2.cvtColor(~img, cv2.COLOR_BGR2GRAY)
cv2.createTrackbar('threshold', 'image', 75, 255, nothing)

ret, thresh_gray = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    shape = detect_marks(img, landmark_model, rect)
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    mask, end_points_left = eye_on_mask(mask, left, shape)
    mask, end_points_right = eye_on_mask(mask, right, shape)
    mask = cv2.dilate(mask, kernel, 5)

    area = cv2.contourArea(contour)
    rect = cv2.boundingRect(contour)
    x, y, width, height = rect
    radius = 0.25 * (width + height)
    # eyes
    eyes = cv2.bitwise_and(img, img, mask=mask)
    mask = (eyes == [0, 0, 0]).all(axis=2)
    eyes[mask] = [255, 255, 255]
    mid = (shape[42][0] + shape[39][0]) // 2
    eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
    threshold = cv2.getTrackbarPos('threshold', 'image')

    area_condition = (100 <= area <= 200)
    symmetry_condition = (abs(1 - float(width)/float(height)) <= 0.2)
    fill_condition = (abs(1 - (area / (math.pi * math.pow(radius, 2.0)))) <= 0.3)
    contouring = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cnt = max(cnts, key=cv2.contourArea)
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    if right:
        cx += mid
    cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
    pos = find_eyeball_position(end_points, cx, cy)
    return pos
    eyeball_pos_left = contouring(thresh[:, 0:mid], mid, img, end_points_left)
    if left != 0:
        text = ''
        if left == 1:
            print('Looking left')
            text = 'Looking left'
        elif left == 2:
            print('Looking right')
            text = 'Looking right'
        elif left == 3:
            print('Looking up')
            text = 'Looking up'
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (30, 30), font,
                    1, (0, 255, 255), 2, cv2.LINE_AA)

    if area_condition and symmetry_condition and fill_condition:
        cv2.circle(img, (int(x + radius), int(y + radius)), int(1.3*radius), (0,180,0), -1)

cv2.imshow('Pupil Detector', img)
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
c = cv2.waitKey()
cv2.destroyAllWindows()