# main packages
import os
import sys
import requests
import cv2
imoprt dlib
import tensorflow as tf
import tensorflow as keras
import numpy as np
# other files
from loadimg import FACIAL_LANDMARKS_IDXS
from loadimg import FACIAL_LANDMARKS_5_IDXS
from loadimg import FACIAL_LANDMARKS_68_IDXS
from loadimg import visualize_facial_landmarks
from loadimg import rect_to_bb
from loadimg import shape_to_np
    # [ LOADING STUFF]
        # HAAR cascade classifiers
cascade_face_1 = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
cascade_face_2 = cv2.CascadeClassifier('models/haarcascade_profileface.xml')
cascade_face_3 = cv2.CascadeClassifier('models/haarcascade_frontalface_alt_tree.xml')
cascade_face_4 = cv2.CascadeClassifier('models/haarcascade_frontalface_alt.xml')
cascade_face_5 = cv2.CascadeClassifier('models/haarcascade_frontalface_alt2.xml')
cascade_eye_left_1 = cv2.CascadeClassifier('models/haarcascade_left_eye_2splits.xml')
cascade_eye_right_1 = cv2.CascadeClassifier('models/haarcascade_right_eye_2splits.xml')
cascade_eye_2 = cv2.CascadeClassifier('models/haarcascade_eye_tree_eyeglasses.xml')
cascade_eye_3 = cv2.CascadeClassifier('models/haarcascade_eye.xml')
cascade_trainer = cv2.CascadeClassifier('opencv-haar-classifier-training.html')
    ## [ RAW IMAGES ]
        # take input from camera, device = 0
cap = cv2.VideoCapture(0)
cv2.namedWindow('YUGA_capture_stream')
    ## [ PROCESS ]
        # convert image to grey
rgb_color = cv2.ctColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 4)
        # detection stuff
face_read = cascade_face_1.detectMultiScale(gray, 1.5, 5)
left_eye = cascade_eye_left_1.detectMultiScale(gray)
    ## [ ESTIMATE ]
        # draw Hough Circles to estimate pupil center

    ## [ APPLY TO RAW STREAM ]
        #camera
    ## [ main ]
while 1:
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        roi_gray2 = gray[ey:ey+eh, ex:ex+ew]
        roi_color2 = img[ey:ey+eh, ex:ex+ew]
        circles = cv2.HoughCircles(roi_gray2,cv2.HOUGH_GRADIENT,1,200,param1=200,param2=1,minRadius=0,maxRadius=0)
        try:
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(roi_color2,(i[0],i[1]),i[2],(255,255,255),2)
                print("drawing circle")
                # draw the center of the circle
                cv2.circle(roi_color2,(i[0],i[1]),2,(255,255,255),3)
        cv2.imshow('YUGA', img)
        if cv2.waitKey(30) & 0xFF == ord('q'):
    break
    ## [ RESULTS ]
        ## algorithm stuff
        # # DLIB
        # for result in only_left_eye:
        #     x = result.left()
        #     y = result.top()
        #     x1 = result.right()
        #     y1 = result.bottom()
        #     cv2.rectangle(img1, (x, y), (x1, y1), (0, 0, 255), 2)
        #     cv2.imshow("dlib", img1)
        # # OpenCV
        # for i in range(only_left_eye.shape[2]):
        #     confidence = faces3[0, 0, i, 2]
        #     if confidence > 0.5:
        #         box = faces3[0, 0, i, 3:7] * np.array([width, height, width, height])
        #         (x, y, x1, y1) = box.astype("int")
        #         cv2.rectangle(img2, (x, y), (x1, y1), (0, 0, 255), 2)
        #         cv2.imshow("dnn", img2)
        # # HAAR
        # for result in only_left_eye:
        #     x, y, w, h = result
        #     x1, y1 = x + w, y + h
        #     cv2.rectangle(img, (x,y), (x1,y1),(0,0,255),2)
        #     cv2.imshow("haar", img3)

#exit + close all open windows created
cap.release()
cv2.destroyAllWindows()