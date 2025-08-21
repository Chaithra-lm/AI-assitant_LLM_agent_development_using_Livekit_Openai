# tests/conftest.py
from dotenv import load_dotenv

# Load your local env vars so tests can see OPENAI_API_KEY
load_dotenv(".env.local", override=True)