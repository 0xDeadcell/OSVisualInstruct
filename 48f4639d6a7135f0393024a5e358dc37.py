import pyautogui
import time

sleep_time = 2

# Step 3
wordpad_icon = pyautogui.locateOnScreen('./buttons/wordpad_icon.png')
pyautogui.click(wordpad_icon)
time.sleep(sleep_time)
print("Success: Step 3")

# Step 5
text_to_type = "Hello, this is an automated message using pyautogui!"
pyautogui.typewrite(text_to_type)
time.sleep(sleep_time)
print("Success: Step 5")

# Step 6
pyautogui.hotkey('ctrl', 's')
time.sleep(sleep_time)
print("Success: Step 6")

# Final success message
print("Automation complete!")
