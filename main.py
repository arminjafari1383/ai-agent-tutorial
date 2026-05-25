from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(
    api_key,
    base_url="https://openrouter.ai/api/v1"
)


while True:
    #code inside this loop will keep on running until manually stopped