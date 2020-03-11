import numpy as np
import cv2

class ShapeDetector:
    shapes = shapes = {
            3: "TRIANGLE",
            4: "SQUARE",
            5: "PENTAGON",
            6: "HEXAGON",
            7: "SEPTAGON"
        }

    def __init__(self):
        pass
    
    def detect_shape(self, contour):
        
        shape = "undef"
        perimeter = cv2.arcLength(contour, True)
        poly_approx = cv2.approxPolyDP(contour, .01 * perimeter, True)

        shape = self.shapes.get(len(poly_approx), "NOT_IMPORTANT_SHAPE")
        if (shape == "SQUARE"):
            (x,y,w,h) = poly_approx
            ar = w/float(h)
            shape = "SQUARE" if ar >= 0.95 and ar <= 1.05 else "RECTANGLE"
