
import cv2 
import numpy as np
import pyautogui
import pydirectinput
import time

cap = cv2.VideoCapture(0)
pydirectinput.FAILSAFE = False
screen_w, screen_h = pyautogui.size()

while True:
    # Take each frame
    ret, frame = cap.read()
    if not ret:
        break

    frame_h, frame_w, _ = frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    (_, _, _, maxLoc) = cv2.minMaxLoc(mask)
    x=0
    y=0
    x = int(maxLoc[0] * (screen_w / frame_w))
    y = int(maxLoc[1] * (screen_h / frame_h))
    if maxLoc[0] != 0:
        pydirectinput.moveTo(x, y)
        print(x,y)
        pydirectinput.click()
        time.sleep(0.1)
    cv2.circle(frame, maxLoc, 20, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('Track Laser', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()