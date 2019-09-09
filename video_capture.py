import numpy as np
import cv2

cap = cv2.VideoCapture(0)
img_index = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Perform operations on the frame
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the modified frame
    #cv2.imshow('frame', gray)
    cv2.imshow('frame', frame)

    # Get keypress index
    key = cv2.waitKey(1)

    if key == 27 or key == ord('q'):
        # Exit on Escape or "q" key press
        break
    elif key == ord('s'):
        cv2.imwrite('pictures/image' + str(img_index) + '.jpeg', frame)
        img_index += 1
        print('Created image:', img_index)

# Release the resources
cap.release()
cv2.destroyAllWindows()
