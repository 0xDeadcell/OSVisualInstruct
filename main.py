import os
import subprocess
import time
import cv2
import mss
import queue
import winshell  # For handling .lnk files
import numpy as np
import pygetwindow as gw
import threading
import keyboard  # You need to install this package
import psutil
import win32gui
import win32process

import sys

from datetime import datetime
from pygetwindow import PyGetWindowException
from pywinauto.application import Application


# Constants and Parameters
EXECUTABLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'executables'))
RECORDINGS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'recordings'))

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

def kill_focused_process():
    try:
        hwnd = win32gui.GetForegroundWindow()  # Get handle to active window
        _, pid = win32process.GetWindowThreadProcessId(hwnd)  # Get the process ID of the active window
        process = psutil.Process(pid)
        process.terminate()  # Terminate the process
        print(f"Terminated process with PID: {pid}")
    except Exception as e:
        print(f"An error occurred while terminating the process: {e}")

def keyboard_listener(start_event, stop_event, kill_event):
    try:
        print("Press CTRL+HOME to start recording.")
        keyboard.wait('ctrl+home')
        start_event.set()
        print("Recording started. Press CTRL+END to stop.")
        keyboard.wait('ctrl+end')
        stop_event.set()
        kill_event.set()  # Signal that the process should be killed
    except KeyboardInterrupt:
        stop_event.set()


def screen_recording(executable_path, app_recording_dir, recording_name, capture_full_screen, start_event, stop_event):
    with mss.mss() as sct:
        start_event.wait()

        frame_count = 0
        monitor = sct.monitors[0] if capture_full_screen else capture_active_window()
        if not monitor:
            print("No active window detected, skipping recording.")
            return

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_file_path = os.path.join(app_recording_dir, f"{recording_name}.mp4")

        out = cv2.VideoWriter(video_file_path, fourcc, 8.0, (monitor['width'], monitor['height']))

        print(f"Recording started for {recording_name}. Press CTRL+END to stop.")
        while not stop_event.is_set():
            # every 5 frames update the monitor in case the window has moved
            if frame_count % 5 == 0 and not capture_full_screen:
                old_monitor = monitor
                monitor = capture_active_window()
                if not monitor:
                    print("Active window lost, stopping recording.")
                    break
                elif (monitor['width'], monitor['height']) != (old_monitor['width'], old_monitor['height']):
                    print("Window resolution changed, adding black bars.")
                    # Handle resolution change with padding if necessary (not implemented here)
                    
            sct_img = sct.grab(monitor)
            if sct_img:
                img = np.array(sct_img)
                img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                out.write(img)
            else:
                print("Failed to capture screen.")

            frame_count += 1

        out.release()
        print(f"Recording stopped for {recording_name}.")

def record_both(executable_path, item_name):
    start_event = threading.Event()
    stop_event = threading.Event()

    recording_name_fullscreen = f"{item_name}_fullscreen"
    recording_name_active_window = f"{item_name}_activewindow"

    fullscreen_thread = threading.Thread(target=screen_recording, args=(executable_path, recording_name_fullscreen, True, start_event, stop_event))
    activewindow_thread = threading.Thread(target=screen_recording, args=(executable_path, recording_name_active_window, False, start_event, stop_event))

    fullscreen_thread.start()
    activewindow_thread.start()

    return start_event, stop_event, fullscreen_thread, activewindow_thread

def main():
    if not os.path.exists(RECORDINGS_DIR):
        os.makedirs(RECORDINGS_DIR)

    executables_queue = queue.Queue()
    for item in os.listdir(EXECUTABLES_DIR):
        executables_queue.put(item)

    while not executables_queue.empty():
        item = executables_queue.get()
        item_path = os.path.join(EXECUTABLES_DIR, item)
        if os.path.isfile(item_path):
            executable_path = winshell.shortcut(item_path).path if item_path.endswith('.lnk') else item_path

            item_name = os.path.splitext(os.path.basename(executable_path))[0]

            application_name = os.path.splitext(os.path.basename(executable_path))[0].lower()
            with mss.mss() as sct:    
                # Get the resolution of the monitor from sct.monitor if we are capturing the full screen
                resolution = str(sct.monitors[0]['width']) + 'x' + str(sct.monitors[0]['height'])
                operating_system = 'win11' if sys.getwindowsversion().major >= 10 else 'win10'

                app_recording_dir = os.path.join(RECORDINGS_DIR, operating_system, resolution, application_name)
                # create the directories for the app_recording_dir
                os.makedirs(app_recording_dir, exist_ok=True)
                app_already_recorded = False
                for f in os.listdir(app_recording_dir):
                    if f.endswith('.mp4'):
                        app_already_recorded = True
                # Skip this executable if it has already been recorded
                if app_already_recorded:
                    print(f"[!] Skipping {item_name} as it has already been recorded.")
                    continue
                        

            start_event = threading.Event()
            stop_event = threading.Event()
            kill_event = threading.Event()  # Used to signal when to kill the process

            process = subprocess.Popen(executable_path, shell=False)
            print(f"Started {executable_path}")

            fullscreen_thread = threading.Thread(target=screen_recording, args=(executable_path, app_recording_dir, f"{item_name}_fullscreen", True, start_event, stop_event))
            activewindow_thread = threading.Thread(target=screen_recording, args=(executable_path, app_recording_dir, f"{item_name}_activewindow", False, start_event, stop_event))

            fullscreen_thread.start()
            activewindow_thread.start()

            keyboard_thread = threading.Thread(target=keyboard_listener, args=(start_event, stop_event, kill_event))
            keyboard_thread.start()

            keyboard_thread.join()
            stop_event.set()  # Signal threads to stop recording

            fullscreen_thread.join()
            activewindow_thread.join()

            if kill_event.is_set():
                kill_focused_process()  # Kill the focused process if indicated

            process.terminate()
            print(f"Finished recording {item_name}. Moving on to the next executable or finishing if none left.")

if __name__ == "__main__":
    main()
