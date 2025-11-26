import cv2

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("Error: No stream open")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30   # fallback value

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
width  = int(stream.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(stream.get(cv2.CAP_PROP_FRAME_HEIGHT))

output = cv2.VideoWriter(
    "assets/0_webcam.mp4",
    fourcc,
    fps,
    (width, height)
)

while(True):
    ret, frame = stream.read()
    if not ret:
        print("Stream interrupted")
        break
    
    frame = cv2.resize(frame, (width, height))
    output.write(frame)
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()