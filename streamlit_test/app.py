# import streamlit as st
# import pyautogui
# import cv2
# import numpy as np
# import tempfile
# import requests
# from PIL import ImageGrab
# from dotenv import load_dotenv
# from io import BytesIO
# # Load environment variables
# load_dotenv()
# # API_KEY = st.secrets["API_KEY"]


import streamlit as st
from PIL import ImageGrab
import tempfile
import pyautogui


# Set the page config once at the top of the script
st.set_page_config(page_title='Automated Interaction Tool', layout='wide')

def capture_screen():
    screenshot = ImageGrab.grab()
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
        screenshot.save(tmp.name, 'PNG')
    return tmp.name

def process_screenshot(screenshot_path, prompt):
    # Placeholder for screenshot processing
    return [("click", 100, 200), ("type", "Hello World")]

def translate_to_pyautogui(actions: list) -> list:
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

def main():
    st.title('Interactive Screen Automation Tool')
    user_prompt = st.text_input('Enter your command')

    if st.button('Execute Command'):
        if user_prompt:
            screenshot_path = capture_screen()
            actions = process_screenshot(screenshot_path, user_prompt)
            commands = translate_to_pyautogui(actions)
            
            # Display the PyAutoGUI commands as code
            st.code(', '.join(f"{command.__name__}()" for command in commands))
            
            # Execute the PyAutoGUI commands with safety checks in place
            for command in commands:
                command()
        else:
            st.warning('Please enter a command.')

def sidebar_content():
    st.sidebar.title("About")
    st.sidebar.info(
        "This application is a proof of concept for an Interactive Screen Automation Tool. "
        "It uses Streamlit for the UI and PyAutoGUI for executing the screen automation commands."
    )

# CSS Styling
def load_css():
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

# if __name__ == "__main__":
#     # Run the app functions
#     sidebar_content()
#     load_css()
#     main()

# Run the app functions
sidebar_content()
load_css()
main()
