import numpy as np
import cv2

with open('intrinsic parameters\\mtx.npy', 'rb') as f:
    mtx = np.load(f)
with open('intrinsic parameters\\dist.npy', 'rb') as f:
    coef = np.load(f)


cap = cv2.VideoCapture("examples\\parallel_BS_15mm.avi")

if (cap.isOpened()==False):
    print("Error at opening the file")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame',frame)
        undistort = cv2.undistort(frame, mtx, coef, None)
        cv2.imshow('Undistorted',undistort)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()