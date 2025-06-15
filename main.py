import os
import sys

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    raise IOError('No prompt has been provided')

responses = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=sys.argv[1],
)

print(responses.text)
print(f"Prompt tokens: {responses.usage_metadata.prompt_token_count}")
print(f"Response tokens: {responses.usage_metadata.candidates_token_count}")
