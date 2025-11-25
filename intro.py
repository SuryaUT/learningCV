import cv2

img = cv2.imread("assets/Birthday.jpeg", cv2.IMREAD_COLOR)
resized = cv2.resize(img, (800, 1000))

cv2.imshow("Boomer", resized)
print(resized.shape)
print(resized[0,0])
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_dog = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imwrite("assets/gray_dog.jpg", gray_dog)