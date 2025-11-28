import cv2
import numpy as np
'''
Displays image and closes window on any key press
Inputs:
- title: string title of image
- img: image to be displayed
Outputs:
- doesn't return anything, just displays image
'''
def showimg(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("assets/shapes.png")
height, width = img.shape[0], img.shape[1]
img = cv2.resize(img, (int(width/2), int(height/2)))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
SHI-TOMASI METHOD:
Use 2-D sliding window to detect deviations in
line trajectories, i.e. corners

OBSERVATIONS:
Works well for the most part but misses some
obvious corners
'''
corners = cv2.goodFeaturesToTrack(gray, maxCorners=50, qualityLevel=0.1, minDistance=50)
corners = np.int0(corners)
for c in corners:
    x,y = c.ravel()
    img = cv2.circle(img, center=(x, y), radius=10, color=(0,0,255), thickness=-1)

'''
HARRIS METHOD:
Uses a sliding window to smooth pixel gradients
and construct 2x2 structure tensor matrix, M. M
is used to calculate R score (det(M) - k(trace(M))^2)
which, if over a threshold, indicates a corner.

OBSERVATIONS:
Seems to work better than the Shi-Tomasi Method.
However, this result is highly dependent on the
input parameters, which could be tweaked for
better accuracy.
'''
corners = cv2.goodFeaturesToTrack(gray, maxCorners=50, qualityLevel=0.01, minDistance=50, 
                                  useHarrisDetector=True, k=0.05)
corners = np.int0(corners)
for c in corners:
    x,y = c.ravel()
    img = cv2.circle(img, center=(x, y), radius=5, color=(0,255,0), thickness=-1)

cv2.imwrite("assets/2_corner_detection.jpg", img)
showimg("CVS", img)