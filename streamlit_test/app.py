import streamlit as st
import pyautogui
import cv2
import numpy as np
import tempfile
import requests
from PIL import ImageGrab
from dotenv import load_dotenv
from io import BytesIO

# Load environment variables
load_dotenv()
API_KEY = st.secrets["API_KEY"]

def capture_screen():
    screenshot = ImageGrab.grab()
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
        screenshot.save(tmp.name, 'PNG')
    return tmp.name

def process_screenshot(screenshot_path, prompt):
    # Here you would process the screenshot with your selected ML model
    # This function is a placeholder for the actual implementation
    # Let's assume it returns a list of actions to be translated into PyAutoGUI commands
    return [("click", 100, 200), ("type", "Hello World")]

def translate_to_pyautogui(actions: list) -> list:
    # This function translates actions into PyAutoGUI commands
    # This is a placeholder for the actual API call and processing logic
    commands = []
    for action in actions:
        if action[0] == "click":
            commands.append(f"pyautogui.click({action[1]}, {action[2]})")
        elif action[0] == "right_click":
            commands.append(f"pyautogui.rightClick({action[1]}, {action[2]})")
        elif action[0] == "double_click":
            commands.append(f"pyautogui.doubleClick({action[1]}, {action[2]})")
        elif action[0] == "scroll_up":
            commands.append(f"pyautogui.scroll(100)")  # Scrolls up by 100 units
        elif action[0] == "scroll_down":
            commands.append(f"pyautogui.scroll(-100)")  # Scrolls down by 100 units
        elif action[0] == "type":
            commands.append(f"pyautogui.typewrite('{action[1]}')")
        elif action[0] == "hotkey":
            keys = ','.join(f"'{key}'" for key in action[1:])
            commands.append(f"pyautogui.hotkey({keys})")
    return commands


# Streamlit interface
st.title('Interactive Screen Automation Tool')

# Text input for the user prompt
user_prompt = st.text_input('Enter your command')

# Button to capture screen and process the command
if st.button('Execute Command'):
    if user_prompt:
        # Capture screen
        screenshot_path = capture_screen()
        # Process screenshot and user prompt
        actions = process_screenshot(screenshot_path, user_prompt)
        # Translate actions to PyAutoGUI commands
        commands = translate_to_pyautogui(actions)

        # Display commands and execute
        st.code(commands)
        
        # Execute the PyAutoGUI commands
        # WARNING: Executing commands with eval() is dangerous and is only being used here for demonstration purposes.
        # A more secure approach should be implemented for actual use.
        for command in commands:
            exec(command)
    else:
        st.warning('Please enter a command.')

if __name__ == '__main__':
    st.set_page_config(page_title='Automated Interaction Tool', layout='wide')
    st.markdown("""
        <style>
        .reportview-container {
            max-width: 1200px;
            padding-top: 5rem;
            padding-right: 1rem;
            padding-left: 1rem;
            padding-bottom: 10rem;
        }
        .reportview-container .main .block-container{
            padding-top: 5rem;
        }
        </style>
        """, unsafe_allow_html=True)
    st.sidebar.title("About")
    st.sidebar.info(
        "This application is a proof of concept for an Interactive Screen Automation Tool. "
        "It uses Streamlit for the UI and PyAutoGUI for executing the screen automation commands."
    )
    app()
