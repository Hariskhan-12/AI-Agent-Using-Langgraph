import os
from dotenv import load_dotenv

load_dotenv()

def load_env(key: str) -> str:
    return os.getenv(key)
