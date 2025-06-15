import os
import sys

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    raise IOError("No prompt has been provided")

user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

responses = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)


prompt_tokens = responses.usage_metadata.prompt_token_count
response_tokens = responses.usage_metadata.candidates_token_count
print(responses.text)
# print(f"Prompt tokens: {prompt_tokens}")
# print(f"Response tokens: {response_tokens}")

if "--verbose" in sys.argv:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
