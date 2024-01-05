import pyautogui
import time

# Step 2: Open WordPad application
pyautogui.press('win')  # Press the Windows key
time.sleep(1)  # Wait for the start menu to appear
pyautogui.typewrite('wordpad')  # Type "wordpad" to search for the application
time.sleep(1)  # Wait for the search results to appear
pyautogui.press('enter')  # Press Enter to open WordPad
time.sleep(2)  # Wait for WordPad to open

# Step 3: Click on the "Save" button
save_button_img = './buttons/save_button.png'  # Replace with the actual path to the save button image
save_button_location = pyautogui.locateOnScreen(save_button_img)
if save_button_location:
    pyautogui.click(save_button_location)
    print('Step 3: Clicked on the "Save" button - Success')
else:
    print('Step 3: Clicked on the "Save" button - Failed')

time.sleep(2)  # Wait for the save dialog window to open

# Step 4: Close the save dialog
cancel_button_img = './buttons/cancel_button.png'  # Replace with the actual path to the cancel button image
cancel_button_location = pyautogui.locateOnScreen(cancel_button_img)
if cancel_button_location:
    pyautogui.click(cancel_button_location)
    print('Step 4: Closed the save dialog - Success')
else:
    print('Step 4: Closed the save dialog - Failed')

time.sleep(2)  # Wait for the cancel button to be clicked

# Step 6: Write a story about AI programmers
story = "Once upon a time, there were AI programmers who developed amazing algorithms."
pyautogui.typewrite(story)
print('Step 6: Wrote a story about AI programmers - Success')

# Step 7: Save the document
pyautogui.hotkey('ctrl', 's')
time.sleep(2)  # Wait for the save dialog to open
pyautogui.typewrite('AI_programmers_story.txt')  # Replace with the desired file name
pyautogui.press('enter')
print('Step 7: Saved the document - Success')

# Step 8: Close WordPad application
pyautogui.hotkey('alt', 'f4')
time.sleep(2)  # Wait for WordPad to close
print('Step 8: Closed WordPad application - Success')
