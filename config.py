import os
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

def get_api_key():
    """Retrieve the Google API key from environment variables."""
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        logging.error("Google API key not found")
        raise ValueError("Google API key not found. Ensure it's set in your .env file.")
    return api_key