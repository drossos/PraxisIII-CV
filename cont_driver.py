from Classes.ShapeDetector import ShapeDetector
from Classes.ColourFilter import ColourFilter 
import cv2
import imutils
import numpy as np
import os

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("F:\OpenProjects\PraxisIII\PraxisIII-CV\\test_vid.mp4")

# colour bounds in HSV values
lower= np.array([30,150,50])
upper = np.array([76,255,180])

def main():
    # Capture frame-by-frame
    ret, img_raw = cap.read()
    #img_raw = cv2.imread("C:/Users/Daniel Personal/Documents/PraxisIII/cvdemo/PraxisIII-CV/Classes/testsquare.png")

    if (img_raw is None):
        pass

    # Filter Out Colour
    cf = ColourFilter()
    cf.filter(upper, lower, img_raw)

    # Convert to easy edge work
    gray = cv2.cvtColor(cf.filtered, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    # Create Contours
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()

    img_raw = draw_contours(cnts, img_raw, sd)

    cv2.imshow("THRESH", thresh)
    cv2.imshow("Shapes", img_raw)

    
def draw_contours(cnts, img_raw, sd):    
    for c in cnts:
            M = cv2.moments(c)
            try:
                cX = int((M["m10"] / M["m00"]))
                cY = int((M["m01"] / M["m00"]))
        
                shape = sd.detect_shape(c)
                if (shape != "NOT_IMPORTANT_SHAPE" and cv2.contourArea(c)>100):
                    cv2.drawContours(img_raw, [c], -1, (0, 255, 0), 2)
                    cv2.putText(img_raw, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (255, 0, 0), 2)
            
                print(shape)
            except:
                print("not closed shape")
    return img_raw


while (1):
    main()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()