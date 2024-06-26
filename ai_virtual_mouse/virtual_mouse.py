import cv2
import numpy
import time
import autopy
import numpy as np

import hand_tracking_module as htm

wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7

pLocX, pLocY = 0, 0
cLocX, cLocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

while True:
    # Find Hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList, bbox = detector.findPosition(img)

    # Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # Check which fingers are up
        fingers = detector.fingersUp()
        # Creating a Frame
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # Only Index finger: Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            # Smoothen Values
            cLocX = pLocX + (x3 - pLocX) / smoothening
            cLocY = pLocY + (y3 - pLocY) / smoothening
            # Move Mouse
            autopy.mouse.move(wScr - cLocX, cLocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            pLocX, pLocY = cLocX, cLocY
        # Both Index and Middle fingers: Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            # Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # Click mouse if distance short
            if length < 30:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

    # Frame rate
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
