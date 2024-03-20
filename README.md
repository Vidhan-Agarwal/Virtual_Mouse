## AI Virtual Mouse

This project implements a virtual mouse controlled by hand gestures using OpenCV, hand tracking, mediapipe, and screen automation libraries.

**Features:**

* **Hand Tracking:** Utilizes a hand tracking module to detect and localize your hand and fingers in the webcam feed.
* **Movement Mode:** Move the mouse cursor on your screen by raising your index finger and dragging it across the frame.
* **Clicking Mode:** Raise both your index and middle fingers together to simulate a left mouse click.
* **Smoothening:** Ensures smooth cursor movement by averaging fingertip positions over a defined number of frames.
* **Frame Rate Display:** Shows the real-time frame rate of the application.

**Requirements:**

* Python 3.x
* OpenCV library (`pip install --upgrade opencv-python`)
* autopy library (`pip install autopy`)
* Mediapipe library(`python -m pip install mediapipe`)
* [hand_tracking_module.py](ai_virtual_mouse/hand_tracking_module.py)

**Instructions:**

1. Download or clone the repository.
2. Install the required libraries.
3. Make sure you have `hand_tracking_module.py` in the same directory or adjust the path in the code.
4. Run the application using `python AI_VIRTUAL_MOUSE.py`.
