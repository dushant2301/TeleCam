import threading
import time
import tkinter as tk
from tkinter import messagebox

from network_monitor import wait_for_internet
from camera import capture_image
import tray

CAPTURE_INTERVAL = 10 # Set to 10 seconds

def ask_for_consent():
    root = tk.Tk()
    root.withdraw() # Hide the main window
    root.attributes("-topmost", True) # Force popup to the front
    
    result = messagebox.askyesno(
        "LaptopWebcam Consent",
        "This application will run in the background and capture an image every 10 seconds, sending it to your Telegram.\n\n"
        "The tray icon will turn RED while capturing.\n\n"
        "Do you authorize this session?"
    )
    root.destroy()
    return result

def monitor_application():
    print("LaptopWebcam background worker started.")
    time.sleep(1) # Give tray time to load
    
    while not tray.stopped.is_set():
        
        # 1. Turn icon red to indicate camera is active
        tray.set_camera_state(True)
        
        # 2. Wait for internet (if no internet, it waits here safely)
        if not wait_for_internet(tray.stopped):
            break
            
        if tray.stopped.is_set():
            break

        # 3. Capture and Send
        print("Capturing image...")
        success = capture_image()
        
        if success:
            print("Image sent successfully to Telegram.")
        else:
            print("Capture or delivery failed.")

        # 4. Turn icon back to green while sleeping
        tray.set_camera_state(False)

        # 5. Wait for 10 seconds, but stop immediately if Exit is clicked
        if tray.stopped.wait(timeout=CAPTURE_INTERVAL):
            break

if __name__ == "__main__":
    
    # # 1. Ask for consent before doing anything
    # if not ask_for_consent():
    #     print("Consent denied. Exiting.")
    #     exit()

    # 2. Start background camera worker
    worker = threading.Thread(target=monitor_application, daemon=True)
    worker.start()

    # 3. Run the tray on the main thread (blocks until Exit is clicked)
    tray.run_tray()

    # 4. Cleanup
    tray.stopped.set()
    worker.join(timeout=5)
    print("Application closed cleanly.")