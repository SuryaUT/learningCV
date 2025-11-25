import cv2

def showimg(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("assets/Birthday.jpeg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (800, 1000))

#Border

bordered = cv2.copyMakeBorder(img, 20, 20, 20, 20, borderType=cv2.BORDER_CONSTANT, value=(100, 50, 30))
showimg("Bordered Boomer", bordered)

#Line
teeth = bordered.copy()
teeth = cv2.line(teeth, (450, 470), (440, 500), color = (0, 0, 200), thickness=10)
teeth = cv2.line(teeth, (440, 470), (440, 500), color = (0, 0, 200), thickness=10)

teeth = cv2.line(teeth, (370, 465), (380, 500), color = (0, 0, 200), thickness=10)
teeth = cv2.line(teeth, (380, 465), (380, 500), color = (0, 0, 200), thickness=10)
showimg("Count-Boomer", teeth)

#Arrow
alien = bordered.copy()
alien = cv2.arrowedLine(alien, (410, 320), (410, 250), color=(0, 200, 0), thickness = 20, tipLength=0.2)
showimg("Gleeb", alien)

#Circle
nerd = bordered.copy()
nerd = cv2.circle(nerd, center = (360, 360), color=(100, 100, 0), radius=30, thickness=10)
nerd = cv2.circle(nerd, center = (480, 360), color=(100, 100, 0), radius=30, thickness=10)
showimg("Nerd", nerd)

#Ellipse
round = bordered.copy()
round = cv2.ellipse(round, center=(500, 600), axes=(100, 200), angle=-30, startAngle=-35, endAngle=200, color=(100, 0, 100), thickness=50)
showimg("Round", round)

#Rectangle
rect = bordered.copy()
rect = cv2.rectangle(rect, pt1=(200, 400), pt2=(600, 600), color=(150, 150, 150), thickness=10)
showimg("Just a Rectangle", rect)

#Text
text = bordered.copy()
text = cv2.putText(text, "Boomer", org=(240, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(200,200,0), thickness=10)
showimg("Boomer", text)