import numpy as np
import cv2

cap = cv2.VideoCapture(1)
epsilon = .01


class ShapeDetector:
    def __init__(self):
        pass
    
    def sides_2_shape(numsides):
        shapes = {
            3: "TRIANGLE",
            4: "SQUARE",
            5: "PENTAGON",
            6: "HEXAGON",
            7: "SEPTAGON"
        }

        return shapes.get(numsides, "NOT_IMPORTANT_SHAPE")

    def detect_shape(self, contour):
        shape = "undef"
        perimeter = cv2.arcLength(contours,True)
        poly_approx = cv2.approxPolyDP(contour, .01 * perimeter, True)

        shape = self.sides_2_shape(poly_approx)
        if (shape == "SQUARE"):
            (x,y,w,h) = poly_approx
            ar = w/float(h)
            shape = "SQUARE" if ar >= 0.95 and ar <= 1.05 else "RECTANGLE"


while(True):
    # Capture frame-by-frame
    ret, img = cap.read()

    img_gry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    edged = cv2.Canny(img_gry, 30, 200)
    cv2.imshow("edges",edged)
    cv2.waitKey(1)

    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 


    polys = []
    for i in contours:
        polys = polys + [cv2.approxPolyDP(i, epsilon, True)]
    
    cv2.drawContours(img, polys, -1, (0, 255, 0), 3) 
    cv2.imshow('Approx Shapes', img) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()