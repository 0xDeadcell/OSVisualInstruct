from dotenv import load_dotenv, find_dotenv, dotenv_values

load_dotenv(find_dotenv())
OPENAI_API_KEY = dotenv_values(".env").get("OPENAI_API_KEY", None)

import openai
from openai import OpenAI
openai.api_key = OPENAI_API_KEY

# Omitted steps:
# Take screenshot
# Chunk screenshot into x amount of sections
# Create a grid overlayed against each chunked screenshot with x,y labels based off the total resolution of the original screenshot, use as large of a font size for the labels as possible
# Save a copy of and provide a link to the model with each of the chunked screenshots
# After the model returns a x,y tuple, feed the x,y tuple with the original prompt back into gpt3.5-turbo with an expected one-line response of the pyautogui code to be run to complete the users action:
# Example Prompt: "Write out a one-liner with pyautogui that performs the action based on the original prompt, and the determined x,y coordinates: 'Original Prompt: What are the x,y coordinates for the "X"/close button for my Windows Explorer application?', 'Vision Assistant Answer: (1420, 680)'"

client = OpenAI()
USER_PROMPT = "What are the x,y coordinates for the 'X'/close button for my Windows Explorer application?"
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {"role": "system",
            "content": "You are a helpful assistant who analyzes screenshots from a computer that may have various applications or windows open, you expertly analyze the images provided and detail which one had what the user was looking for, you will respond with your thought process, which image contained what the user was referring to, and finally a tuple of the X,Y coordinates using the overlayed grid and x and y labels. Helpful Tip: First determine the application/location/task they might be referring to and use that to determine which image contains what they are referring to, then determine the exact spot of the image they want and respond with the X,Y coordinates."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": "https://github.com/0xDeadcell/OSVisualInstruct/blob/main/img1topleft.PNG?raw=true",
                },
                {
                    "type": "image_url",
                    "image_url": "https://github.com/0xDeadcell/OSVisualInstruct/blob/main/img2topright.PNG?raw=true",
                },
                {
                    "type": "image_url",
                    "image_url": "https://github.com/0xDeadcell/OSVisualInstruct/blob/main/img3bottomleft.PNG?raw=true",
                },
                {
                    "type": "image_url",
                    "image_url": "https://github.com/0xDeadcell/OSVisualInstruct/blob/main/img4bottomright.PNG?raw=true",
                },
                
                {
                    "type": "text",
                    "text": USER_PROMPT,
                }
            ],
        }
    ],
    max_tokens=850,
)
print(response.choices[0])

# Example Prompt: "Write out a one-liner with pyautogui that performs the action based on the original prompt, and the determined x,y coordinates: 'Original Prompt: What are the x,y coordinates for the "X"/close button for my Windows Explorer application?', 'Vision Assistant Answer: (1420, 680)'"
# Example Response: "pyautogui.click(1420, 680)"

pyauto_gui_code_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Write out a one-liner with pyautogui that performs the action based on the original prompt, and the determined x,y coordinates provided by the Vision Assistant (you can assume the user ran `import pyautogui` first before running your one-liner so only provide the code and no extra formatting):"},
        {"role": "user", "content": f"'Original Prompt: {USER_PROMPT}'\n\n 'Vision Assistant Answer: {response.choices[0].text}'"}
    ]
    max_tokens=400,
)

import pyautogui
# Yes, this is dangerous (*sweats nervously), but it's just a proof of concept
eval(pyauto_gui_code_response.choices[0].text)