import pyautogui
import time

# Define the automation steps
steps = [
    "Open This PC (Windows + E)",
    "Navigate to the Documents folder",
    "Search for the 'hello.txt' file",
]

# Execute the automation steps
pyautogui.hotkey('win', 'e')
time.sleep(2)
pyautogui.typewrite('Documents')
time.sleep(2)
pyautogui.typewrite('hello.txt')
time.sleep(2)

# Print success
print("Success")

# Print each step number and success
for i, step in enumerate(steps, 1):
    print(f"Step {i}: {step}")
