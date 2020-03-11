from ShapeDetector import ShapeDetector
import cv2
import imutils

cap = cv2.VideoCapture(0)

while (1):
    # Capture frame-by-frame
    ret, img_raw = cap.read()

    gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()

    for c in cnts:
        shape = sd.detect_shape(c)
        cv2.drawContours(img_raw, [c], -1, (0, 255, 0), 2)
        try:
            cv2.putText(img_raw, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
    0.5, (255, 255, 255), 2)
        except:
            print("not closed shape")
        
    
    cv2.imshow("Shapes", img_raw)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
    

