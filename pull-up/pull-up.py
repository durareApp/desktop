import cv2
import mediapipe as mp
import numpy as np
import time

WAIT_TIME = 5
OFFSET = 12

cap = cv2.VideoCapture(0)

mp_pose = mp.solutions.pose  # type: ignore
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

counter = 0
state = "DOWN"
bar_y = None

start_time = None
counting_started = False

WINDOW_NAME = "Pull-Up"
cv2.namedWindow(WINDOW_NAME)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(rgb)

    if results.pose_landmarks:
        lm = results.pose_landmarks.landmark

        nose_y = int(lm[mp_pose.PoseLandmark.NOSE].y * h)
        left_wrist_y = int(lm[mp_pose.PoseLandmark.LEFT_WRIST].y * h)
        right_wrist_y = int(lm[mp_pose.PoseLandmark.RIGHT_WRIST].y * h)

        bar_y = int((left_wrist_y + right_wrist_y) / 2)

        cv2.circle(frame, (w // 2, nose_y), 6, (0, 255, 0), -1)
        cv2.line(frame, (0, bar_y), (w, bar_y), (0, 0, 255), 2)

        if not counting_started:
            if start_time is None:
                start_time = time.time()

            elapsed = time.time() - start_time
            remaining = max(0, int(WAIT_TIME - elapsed))

            cv2.putText(frame,
                        f"Hold Position... {remaining}",
                        (30, 90),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0,
                        (0, 255, 255),
                        3)

            if elapsed >= WAIT_TIME:
                counting_started = True
                state = "DOWN"

        else:
            if nose_y < bar_y - OFFSET:
                state = "UP"

            elif nose_y > bar_y + OFFSET and state == "UP":
                counter += 1
                state = "DOWN"

    cv2.putText(frame,
                f"Pull-Ups: {counter}",
                (30, 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (255, 255, 0),
                3)

    cv2.putText(frame,
                f"State: {state}",
                (30, 130),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (200, 200, 200),
                2)

    cv2.imshow(WINDOW_NAME, frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
