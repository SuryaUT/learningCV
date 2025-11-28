import cv2
import os

#Load cascades
face_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
eye_cascade   = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

def detect_features(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:

        #Draw face bounding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

        #Extract ROI
        face_color = frame[y:y+h, x:x+w]
        face_gray  = gray[y:y+h, x:x+w]

        #Detect smiles
        smiles = smile_cascade.detectMultiScale(face_gray, 2.5, 8)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(face_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 5)

        #Detect eyes
        eyes = eye_cascade.detectMultiScale(face_gray, 2.5, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 5)

    return frame


#Initialize webcam
stream = cv2.VideoCapture(0)
if not stream.isOpened():
    print("Error: Could not open webcam.")
    exit()

#FPS fallback if webcam returns 0
fps = stream.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30

width  = int(stream.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(stream.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter("assets/3_face_detection.mp4", fourcc, fps, (width, height))

#Check if stream is working
if not output.isOpened():
    print("Error: VideoWriter failed to open!")
    stream.release()
    exit()


while True:
    ret, frame = stream.read()
    if not ret:
        print("Stream interrupted.")
        break

    processed = detect_features(frame)

    #Write to video file
    output.write(processed)

    cv2.imshow("Face Detection", processed)

    if cv2.waitKey(1) == ord('q'):
        break


#Shutdown
stream.release()    
cv2.destroyAllWindows()