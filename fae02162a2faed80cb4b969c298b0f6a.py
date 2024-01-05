import pyautogui
import time

# Step 1: Open the start menu
pyautogui.hotkey('win', 's')
time.sleep(2)
print("Step 1: Success")

# Step 2: Search for notepad and open it
pyautogui.typewrite('notepad')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
print("Step 2: Success")

# Step 3: Wait for the notepad window to open
notepad = pyautogui.getWindowsWithTitle('Untitled - Notepad')[0]
notepad.wait('visible')
print("Step 3: Success")

# Step 4: Click on the notepad window to ensure it's in focus
notepad.click()
time.sleep(2)
print("Step 4: Success")

# Step 5: Type the desired text into the notepad
pyautogui.typewrite("This is the desired text")
time.sleep(2)
print("Step 5: Success")

# Step 6: Save the notepad file
pyautogui.hotkey('ctrl', 's')
time.sleep(2)
print("Step 6: Success")

# Step 7: Close the notepad application
pyautogui.hotkey('alt', 'f4')
time.sleep(2)
print("Step 7: Success")
