import cv2
import mediapipe as mp
import os

#Init MediaPipe Modules
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

#Mode Select (Detection / Mesh)
mode = 'd'

#Open Webcam
stream = cv2.VideoCapture(0)
if not stream.isOpened():
    print("Error: Could not open webcam.")
    exit()

#Get Video Properties
fps = stream.get(cv2.CAP_PROP_FPS) or 30
width  = int(stream.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(stream.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Init Video Writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("assets/4_mediapipe_face_detection.mp4", fourcc, fps, (width, height))
if not output.isOpened():
    print("Error: VideoWriter failed to open.")
    stream.release()
    exit()

#Init Models
face_detector = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

#Main Loop
while True:
    ret, frame = stream.read()
    if not ret:
        print("Stream interrupted.")
        break

    #Convert To RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Face Detection Mode
    if mode == 'd':
        results = face_detector.process(rgb)

        #Draw Detection
        if results.detections:
            for det in results.detections:
                mp_draw.draw_detection(frame, det)

        #Detection Label
        cv2.putText(frame, "Face Detection (press 'm')",
                    (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0,255,0), 2)

    #Face Mesh Mode
    elif mode == 'm':
        results = face_mesh.process(rgb)

        #Draw Mesh
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                mp_draw.draw_landmarks(
                    frame,
                    faceLms,
                    mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_draw.DrawingSpec(
                        thickness=1, circle_radius=1)
                )

        #Mesh Label
        cv2.putText(frame, "Face Mesh (press 'd')",
                    (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0,255,255), 2)

    #Write Frame
    output.write(frame)

    #Show Frame
    cv2.imshow("Face Modes", frame)

    #Key Input
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('d'):
        mode = 'd'
    elif key == ord('m'):
        mode = 'm'

#Shutdown
stream.release()
cv2.destroyAllWindows()