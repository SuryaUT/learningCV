import cv2
import mediapipe as mp

#initialize hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

#initialize video capture
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30   # fallback value

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

output = cv2.VideoWriter(
    "assets/1_handtracking.mp4",
    fourcc,
    fps,
    (width, height)
)

#capture, display, and save webcam + handtracking video
while True:
    ret, frame = cap.read()
    if not ret:
        print("Stream interrupted")
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

    output.write(frame)
    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) == ord('q'):
        break

#end webcam stream
cap.release()
cv2.destroyAllWindows()