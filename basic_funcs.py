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

#Read image
img = cv2.imread("assets/Birthday.jpeg", cv2.IMREAD_COLOR)

#Resize
img = cv2.resize(img, (800, 1000))
showimg("Resized Boomer", img)

#Crop
height, width = img.shape[0], img.shape[1]
errorh = height/10
errorw = width/8
cropped = img[int((height-50)/2-2*errorh):int((height-50)/2+errorh),int(width/2-errorw):int(width/2+errorw)]
showimg("Happy Boomer", cropped)

#Rotate
rotated = cv2.rotate(img, cv2.ROTATE_180)
showimg("Upside-Down Boomer", rotated)

M = cv2.getRotationMatrix2D(center = (width/2, height/2), angle = 123, scale=1)
rotated = cv2.warpAffine(img, M, (width, height))
showimg("Idek Boomer", rotated)

#Translate
tx = width/4
ty = -height/3

M = np.array([[1, 0, tx],
              [0, 1, ty]])

translated = cv2.warpAffine(img, M, (width, height))
showimg("Bommer Moved", translated)