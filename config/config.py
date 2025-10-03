import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY") # CONVERTING ENV VARIABLE TO NORMAL VARIABLE
MODEL_NAME = "llama-3.1-8b-instant"
 