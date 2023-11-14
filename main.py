import os
import subprocess
import time
import cv2
import mss
import numpy as np
import pygetwindow as gw
from datetime import datetime

# Constants and Parameters
EXECUTABLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'executables'))  # Directory containing executables
RECORDINGS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'recordings'))    # Directory to save recordings
RECORD_TIME = 60  # Recording duration in seconds

def capture_active_window():
    active_win = gw.getActiveWindow()
    if active_win:
        return {
            "left": active_win.left,
            "top": active_win.top,
            "width": active_win.width,
            "height": active_win.height
        }
    else:
        return None

def screen_recording(executable_path, recording_name, capture_full_screen=True):
    with mss.mss() as sct:
        monitor = sct.monitors[1] if capture_full_screen else capture_active_window()
        if not monitor:
            print("No active window detected, skipping recording.")
            return

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(f'{RECORDINGS_DIR}/{recording_name}.avi', fourcc, 8.0, (monitor['width'], monitor['height']))

        # Start the executable
        process = subprocess.Popen(executable_path, shell=True)

        start_time = time.time()
        while time.time() - start_time < RECORD_TIME:
            img = np.array(sct.grab(monitor))
            out.write(img)

        # Clean up
        process.terminate()
        out.release()
        #cv2.destroyAllWindows()

def main():
    if not os.path.exists(RECORDINGS_DIR):
        os.makedirs(RECORDINGS_DIR)

    for executable in os.listdir(EXECUTABLES_DIR):
        executable_path = os.path.join(EXECUTABLES_DIR, executable)
        if os.path.isfile(executable_path):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            recording_name_fullscreen = f"{os.path.splitext(executable)[0]}_fullscreen_{timestamp}"
            recording_name_active_window = f"{os.path.splitext(executable)[0]}_activewindow_{timestamp}"
            
            # Record the full screen
            screen_recording(executable_path, recording_name_fullscreen, capture_full_screen=True)
            # Record the active window
            screen_recording(executable_path, recording_name_active_window, capture_full_screen=False)

if __name__ == "__main__":
    main()
