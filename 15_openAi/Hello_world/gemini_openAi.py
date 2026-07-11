import os
from dotenv import load_dotenv

from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise SystemExit("Set GOOGLE_API_KEY in .env file before running this script.")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain to me how AI works",
)

print(response.text)