# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 15:15:48 2018

@author: gcervant
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,100,70])
    upper_red = np.array([0,100,100])
    
    dark_red = np.array([0,100,0])
    upper_red = np.array([200,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    kernel = np.ones((15,15), np.float32)/255
    smoothed = cv2.filter2D(res, -1, kernel)
    
    blur = cv2.GaussianBlur(res, (5,5), 0)
    
    cv2.imshow('Input', frame)
    #cv2.imshow('Color Mask', mask)
    cv2.imshow('Result', res)
    cv2.imshow('smoothed', res)
    cv2.imshow('blurred', blur)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()
