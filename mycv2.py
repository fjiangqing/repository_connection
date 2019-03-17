# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:24:41 2018

@author: fjiangqing
"""

import cv2


cameraCapture = cv2.VideoCapture(0)
success, frame = cameraCapture.read()
cv2.imwrite("cat2.jpg", frame)
cameraCapture.release()

#raspistill -o image.jpg