import pyautogui
import time

# Set the sleep time as 2 seconds after every instruction
pyautogui.PAUSE = 2

# Locate and open Notepad using the start menu or desktop shortcut
pyautogui.press('win')
pyautogui.typewrite('notepad')
pyautogui.press('enter')

# Wait for Notepad to open
# Make sure to save a screenshot of the Notepad window and name it 'notepad_window.png' in './buttons' directory
notepad_window_location = pyautogui.locateOnScreen('./buttons/notepad_window.png')
while notepad_window_location is None:
    time.sleep(2)
    notepad_window_location = pyautogui.locateOnScreen('./buttons/notepad_window.png')

pyautogui.click(notepad_window_location)

# Type the desired text into Notepad
pyautogui.typewrite("Hello, World!")

# Save the file with a specific name and location
pyautogui.hotkey('ctrl', 's')
pyautogui.typewrite('C:\\path\\to\\save\\file.txt') # Replace with your desired file path and name
pyautogui.press('enter')

# Close Notepad
pyautogui.hotkey('alt', 'f4')

print("Success")
