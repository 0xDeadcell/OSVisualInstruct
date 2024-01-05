import pyautogui
import time

# Step 2: Open Notepad
pyautogui.press('win')
pyautogui.typewrite('notepad')
pyautogui.press('enter')
time.sleep(2)

# Step 3: Wait for Notepad to open
# You can use a delay or check for a specific window title
time.sleep(2)

# Step 4: Typing alphabets from a to z
for char in range(97, 123):
    pyautogui.typewrite(chr(char))
    time.sleep(2)

# Step 5: Save the file and close Notepad
pyautogui.hotkey('ctrl', 's')
time.sleep(2)
pyautogui.typewrite('./buttons')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('alt', 'f4')

print('Success!')
