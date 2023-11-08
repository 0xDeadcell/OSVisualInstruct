# import streamlit as st
# import pyautogui
# import cv2
# import numpy as np
# import tempfile
# import requests
# from PIL import ImageGrab
# from io import BytesIO

from dotenv import load_dotenv, find_dotenv, dotenv_values
# Load environment variables
load_dotenv(find_dotenv())
# try to load the .env file from ../.env
load_dotenv(find_dotenv("../.env"))
# Get the API key from the .env file
OPENAI_API_KEY = dotenv_values(".env").get("OPENAI_API_KEY", None)
if not OPENAI_API_KEY:
    OPENAI_API_KEY = dotenv_values("../.env").get("OPENAI_API_KEY", None)

# print(OPENAI_API_KEY)
# # API_KEY = st.secrets["API_KEY"]
# https://0xdeadcell-osvisualinstruct-streamlit-testapp-4p4vge.streamlit.app/
import openai
# openai.api_key = OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY
from openai import OpenAI
import base64
import requests

import streamlit as st
from PIL import ImageGrab
import tempfile
import pyautogui


# Set the page config once at the top of the script
st.set_page_config(page_title='Automated Interaction Tool', layout='wide')

def capture_screen():
    try:
        screenshot = ImageGrab.grab()
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
            screenshot.save(tmp.name, 'PNG')
        return tmp.name
    except OSError:
        st.error('Unable to capture screenshot. Please try again.')
        return None

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def process_screenshot(screenshot_path, prompt):
    # Spinning wait message
    st.info('(TODO) Processing screenshot... with prompt: ' + prompt)

    USER_PROMPT = prompt + ". Respond only with the coordinates in the format: (x, y)"
    # client = OpenAI()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant who analyzes screenshots from a computer that may have various applications or windows open. You expertly analyze the images provided and detail which one had what the user was looking for. You will respond with your thought process, which image contained what the user was referring to, and finally a tuple of the X,Y coordinates using the overlayed grid and x and y labels. Helpful Tip: First determine the application/location/task they might be referring to and use that to determine which image contains what they are referring to, then determine the exact spot of the image they want and respond with the X,Y coordinates. The X,Y Coordinates should be the last line of your response and start exactly LIKE \"COORDS: \" followed by the pixel value coordinates in the x,y format: (1560,820)"
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encode_image(screenshot_path)}"
                        }
                    },
                    {
                        "type": "text",
                        "text": USER_PROMPT
                    }
                ]
            }
        ],
        "max_tokens": 1200
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        message_content = response_data.get('choices', [{}])[0].get('message', {}).get('content')
        # st.info(f"[+] [ORIGINAL API Response]\n{response_data}")
    else:
        st.error(f"Error: {response.json()['error']}")
        return None

    st.info(f"[+] [API Response]\n{message_content}")
    return message_content if message_content else None
    # Placeholder for screenshot processing
    # return "(TODO) Details about the screenshot, and what windows are open or x,y coordinates of the buttons, etc."

def generate_llm_actions(llm_details, prompt):
    # Combine the screenshot details with the prompt, make an API call to the LLM, and return the actions in a list, example below
    
    # Placeholder for LLM actions, later will need to tell the LLM to comma separate the actions
    # screenshot_details = ["Open notepad", "click on the text area", "type \"Hello World\"", "press the hotkey \"ctrl+s\"", "type \"hello_world.txt\"", "press enter", "close notepad"]
    try:
        screenshot_details = prompt.split(", ")
    except Exception as e:
        st.error(f"Error: {e}")
        screenshot_details = []
    
    return screenshot_details # Example: 

def convert_text_to_pyautogui_actions(text: str) -> list:
    actions = []
    client = OpenAI()
    if not text:
        text = "Open notepad, click on the text area, type \"Hello World\", press the hotkey \"ctrl+s\", type \"hello_world.txt\", press enter, close notepad"

    system_message = "Write out a comma separated list of one-liner solutions with pyautogui that performs each individual action based on the users prompt, if one of the actions in the prompt needs you to click then respond only with \"screenshot+ACTION\" for that comma separated value (you can assume the user ran `from pyautogui import *` first before running your one-liner so only provide the code and no extra formatting), finally remember to comma separate each action. VALID_ACTIONS: 'click', 'right_click', 'double_click', 'scroll_up', 'scroll_down', 'typewrite', 'press', 'hotkey'."
    
    # The last user action and expected assistant response are appended to the system message
    system_message += "\nExample user query: " + text
    system_message += "\nExpected assistant action: screenshot+open notepad, typewrite(\"Hello World\"), hotkey(\"ctrl+s\"), typewrite(\"hello_world.txt\"), press(\"enter\"), hotkey(\"alt+f4\")."

    pyauto_gui_code_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": text}
        ],
        max_tokens=1800
    )
    # Yes, this is dangerous (*sweats nervously), but it's just a proof of concept
    response = pyauto_gui_code_response.choices[0].message.content
    st.info(f"[+] TASKS:")
    for i, task in enumerate(response.split(", ")):
        st.info(f"[{i}.] {task}")
    
    # Assuming pyauto_gui_code_response has already been set with a valid response from the API
    response = pyauto_gui_code_response.choices[0].message.content
    actions = []

    for action in response.split(", "):
        if "screenshot+" in action:
            action = action.replace("screenshot+", "")
            new_screenshot_path = capture_screen()
            coordinates = process_screenshot(new_screenshot_path, f"provide the x,y coordinates in order to: {action}")
            
            # Extract the coordinates following "COORDS: "
            coord_string = coordinates.split("COORDS: ")[-1]
            
            # Remove any parentheses and extra whitespace, then split into individual numbers
            coord_string = coord_string.translate({ord(i): None for i in '() '})
            parsed_coordinates = coord_string.split(",")
            
            # Convert the coordinate strings to integers
            try:
                x_coord = int(parsed_coordinates[0])
                y_coord = int(parsed_coordinates[1])
            except ValueError as e:
                st.error(f"Error converting coordinates to integers: {e}")
                # Provide default coordinates if parsing fails
                x_coord, y_coord = 640, 360
            
            # Append the click action with coordinates
            actions.append(["click", x_coord, y_coord])
        else:
            # Assuming other actions do not require coordinate parsing and are just strings
            # You may need to adapt this part depending on the format of other actions
            action_command = action.split("(")[0]
            action_args = action.split("(")[1].rstrip(')').split(", ") if "(" in action else []
            actions.append([action_command] + action_args)

    # Translate the structured actions into pyautogui commands
    pyautogui_commands = translate_to_pyautogui(actions)
    return pyautogui_commands

def translate_to_pyautogui(actions: list) -> list:
    commands = []
    # pyautogui delay set to 0.5 seconds, will pause for 0.5 seconds after each pyautogui command
    commands.append("pyautogui.PAUSE = 0.5")
    for action in actions:
        if action[0] == "click":
            commands.append(f"pyautogui.click({action[1]}, {action[2]})")
        elif action[0] == "right_click":
            commands.append(f"pyautogui.rightClick({action[1]}, {action[2]})")
        elif action[0] == "double_click":
            commands.append(f"pyautogui.doubleClick({action[1]}, {action[2]})")
        elif action[0] == "scroll_up":
            commands.append("pyautogui.scroll(100)")  # Scrolls up by 100 units
        elif action[0] == "scroll_down":
            commands.append("pyautogui.scroll(-100)")  # Scrolls down by 100 units
        elif action[0] == "typewrite":
            commands.append(f"pyautogui.typewrite('{action[1]}')")
        elif action[0] == "press":
            commands.append(f"pyautogui.press('{action[1]}')")
        elif action[0] == "hotkey":
            # Split by the + sign and surround each key with single quotes
            keys = ', '.join([f"'{key}'" for key in action[1:]])
            # keys = ', '.join([f"'{key}'" for key in action[1:]])
            commands.append(f"pyautogui.hotkey({keys})")

    return commands

def main():
    st.title('Interactive Screen Automation Tool')
    user_prompt = st.text_input('Enter your prompt')

    if st.button('Complete Action'):
        if user_prompt:
            screenshot_path = capture_screen()
            llm_details = process_screenshot(screenshot_path, user_prompt)
            # Pop up message telling the user we are using our own prompt for testing
            # user_prompt = '''Open notepad, click on the text area, type \"Hello World\", press the hotkey \"ctrl+s\", type \"hello_world.txt\", press enter, close notepad'''
            # st.info('Using the following prompt for testing: \n' + user_prompt)
            # action_details = generate_llm_actions(llm_details, user_prompt)
            action_details = f"explained details: {llm_details}\n" + f"user_prompt: {user_prompt}"
            commands = convert_text_to_pyautogui_actions(action_details)
            
            # Display the PyAutoGUI commands as code
            for command in commands:
                st.code(command)
            
            # Execute the PyAutoGUI commands with safety checks in place
            for command in commands:
                # Using exec() should be replaced with direct calls to pyautogui functions for security reasons.
                exec(command)  # Use exec to run the string as a command
        else:
            st.warning('Please enter a prompt.')

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

if __name__ == "__main__":
    # Run the app functions
    sidebar_content()
    load_css()
    main()

# # Run the app functions
# sidebar_content()
# load_css()
# main()
