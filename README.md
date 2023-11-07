# OSVisualInstruct


Recreating a Windows OS version of w/out access to the target OS (aside from HDMI, and USB devices such as keyboard/mouse):
https://www.youtube.com/watch?v=QXJ7rImz-Wk

![AI To Control Computer](https://gifrun.blob.core.windows.net/temp/7ed413d0b0f04fe194d16019387b4112.gif)

### Foreseeable challenges using the current resources and technologies for the POC mainly come from [limitations](https://platform.openai.com/docs/guides/vision#:~:text=While%20GPT%2D4,submission%20of%20CAPTCHAs.), in the OpenAI Vision model:
Big text: Enlarge text within the image to improve readability, but avoid cropping important details.


### Potential Solutions to Foreseeable challenges
> Chunk the screenshot into large sections or grids and have the Vision Model identify the portion of the image the user is talking about recursively until the model is comfortable it has found the general area the user is refering to, use that small chunked section to calculate the coordinates that the model/api should return.

#### Example


### Resources:

https://github.com/haotian-liu/LLaVA (Potential Open Source Alternative to Vision, but will likely need to be fine-tuned for this use case)

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


