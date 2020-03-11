import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, img = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Range for upper range
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    output = cv2.bitwise_and(img, img, mask=mask)

    upper = [-1,-1]
    lower = [-1,-1]

    for i in range(1,len(output)):
        for j in range(1,len(output[i])):
            if output[i][j][0] > 0 and upper == [-1,-1]:
                upper = [i,j]
            elif output[i][j][0] > 0:
                lower = [i, j]

    cv2.rectangle(output, (upper[1], upper[0]), (lower[1], lower[0]), color=(0, 255, 0), thickness=3)
    cv2.imshow("images", output)

    # Display the resulting frame
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()