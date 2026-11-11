import cv2
import os
import time
from datetime import datetime
from telegram import send_photo

CAPTURE_DIR = "captures"

def capture_image():
    os.makedirs(CAPTURE_DIR, exist_ok=True)

    # CAP_DSHOW makes opening the camera much faster on Windows
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not camera.isOpened():
        print("Camera unavailable!")
        return False

    try:
        # Allow camera to adjust lighting for a split second
        time.sleep(0.3) 
        
        success, frame = camera.read()

        if not success:
            print("Unable to capture image!")
            return False

        filename = datetime.now().strftime("capture_%Y%m%d_%H%M%S.jpg")
        image_path = os.path.join(CAPTURE_DIR, filename)

        if not cv2.imwrite(image_path, frame):
            print("Image could not be saved!")
            return False

        print("Image saved:", image_path)
        return send_photo(image_path)

    finally:
        camera.release()