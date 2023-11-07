﻿# OSVisualInstruct


Recreating a Windows OS version of w/out access to the target OS (aside from HDMI, and USB devices such as keyboard/mouse):
https://www.youtube.com/watch?v=QXJ7rImz-Wk

![AI To Control Computer](https://gifrun.blob.core.windows.net/temp/7ed413d0b0f04fe194d16019387b4112.gif)


Resources:

https://openai.com/blog/new-models-and-developer-products-announced-at-devday
https://platform.openai.com/docs/guides/vision
```py
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                    "type": "image_url",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])
```

https://github.com/haotian-liu/LLaVA
