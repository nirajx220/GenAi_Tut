import os

from dotenv import load_dotenv
from groq import GroqClient

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise SystemExit("Set GROQ_API_KEY in your .env file before running this script.")

client = GroqClient(api_key=api_key)
