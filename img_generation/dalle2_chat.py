from load_dotenv import load_dotenv
import os
import openai

load_dotenv()

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"])
