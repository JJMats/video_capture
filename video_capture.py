import numpy as np
import argparse, cv2, os
import signal, sys

#def signal_handler(sig, frame):
#  sys.exit(0)

def check_for_existing_file(fn):
    video_path = 'videos/' + fn
    if os.path.exists(video_path) and os.path.isfile(video_path):
        return True

    return False


# Parse arguments
parser = argparse.ArgumentParser(description="Process flags")
parser.add_argument('-o', dest='outfile', type=str, default='out', help="Output filename")
#parser.add_argument('r', dest='rate', type=str, default=5, help="Frame record rate - frames per second")
args = parser.parse_args()


# Check for existing file and append a number to the end if it exists
output_fn = args.outfile
video_index = 1
while(check_for_existing_file(output_fn)):
    # TODO: Strip the file extension if necessary
    output_fn = output_fn + str(video_index)

# Add file extension
output_fn = 'videos/' + output_fn + '.mp4'

cap = cv2.VideoCapture(0)


# Define the codec and create the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'FFV1')
out = cv2.VideoWriter(output_fn, fourcc, 20.0, (640, 480))

# Record the video from the camera
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:

        # Perform operations on the frame
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.flip(frame, 0)

        # Write the frame
        out.write(frame)

        # Display the modified frame
        #cv2.imshow('frame', gray)
        #cv2.imshow('frame', frame)

        # Get keypress index
        key = cv2.waitKey(1)

        if key == 27 or key == ord('q'):
            # Exit on Escape or "q" key press
            break

        if not signal.SIGINT:
            print("Received SIGINT")
            break


# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()
