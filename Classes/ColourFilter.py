import cv2
import numpy as np

class ColourFilter:
    hsv = []
    mask = []
    filtered = []

    def __init__(self):
        pass
    
    def filter(self, upper, lower, img):
        self.hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        self.mask = cv2.inRange(self.hsv, lower, upper)
        self.filtered = cv2.bitwise_and(img,img,mask=self.mask)