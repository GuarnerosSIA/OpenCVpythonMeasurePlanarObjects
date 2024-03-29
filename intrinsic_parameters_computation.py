import numpy as np
import cv2 as cv
import glob
from tempfile import TemporaryFile

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
squareSize=25 # PDF file says this measure
n_squares = 7 # number of squares of the shortest side
m_squares = 10 # number of squares of the largest side

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((n_squares*m_squares,3), np.float32) # PDF chess have another set of dimensions
objp[:,:2] = np.mgrid[0:m_squares,0:n_squares].T.reshape(-1,2)*squareSize#milimetros
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('chessboard images\\11x8\\*.png')
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (m_squares,n_squares), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (m_squares,n_squares), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(100)

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

img = cv.imread('examples\\test.jpg')
h,  w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
# undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
cv.imwrite('examples\\undistorted.png', dst)
cv.imwrite('examples\\distorted.png', img)
# crop the image
#x, y, w, h = roi
#dst = dst[y:y+h, x:x+w]
# undistort
mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
# crop the image
#x, y, w, h = roi
#dst = dst[y:y+h, x:x+w]
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "total error: {}".format(mean_error/len(objpoints)) )

params_folders = "intrinsic parameters\\"

with open(params_folders + 'mtx.npy', 'wb') as f:
    np.save(f, mtx)
with open(params_folders + 'rvecs.npy', 'wb') as f:
    np.save(f, rvecs)
with open(params_folders + 'tvecs.npy', 'wb') as f:
    np.save(f, tvecs)
with open(params_folders + 'dist.npy', 'wb') as f:
    np.save(f, dist)
    
cv.destroyAllWindows()