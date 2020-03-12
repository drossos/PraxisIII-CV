from ShapeDetector import ShapeDetector
import cv2
import imutils
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    # Capture frame-by-frame
    ret, img_raw = cap.read()
    #img_raw = cv2.imread("C:/Users/Daniel Personal/Documents/PraxisIII/cvdemo/PraxisIII-CV/contour/testsquare.png")

    if (img_raw is None):
        pass
    # Our operations on the frame come here
    #img_raw = cv2.cvtColor(img_raw, cv2.COLOR_BGR2HSV)

    # Range for upper range
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([255, 100, 100])
    output = cv2.inRange(img_raw, lower_red, upper_red)

    #gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(output, 60, 255, cv2.THRESH_BINARY)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()

    for c in cnts:

        M = cv2.moments(c)
        try:
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
    
            shape = sd.detect_shape(c)
            if (shape != "NOT_IMPORTANT_SHAPE" and cv2.contourArea(c)>100):
                cv2.drawContours(output, [c], -1, (0, 255, 0), 2)
                cv2.putText(output, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (255, 0, 0), 2)
        
            print(shape)
        except:
            print("not closed shape")

    cv2.imshow("THRESH", output)
    cv2.imshow("Shapes", img_raw)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
    

