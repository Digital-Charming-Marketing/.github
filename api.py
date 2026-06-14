import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
from google import genai

load_dotenv()


def require_key(name: str) -> str:
    """Fetch a required environment variable or fail with a clear message."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Missing {name}. Add it to your .env file (see .env.example)."
        )
    return value


openai_client = OpenAI(
    api_key=require_key("OPENAI_API_KEY"),
)

anthropic_client = anthropic.Anthropic(
    api_key=require_key("ANTHROPIC_API_KEY"),
)

gemini_client = genai.Client(
    api_key=require_key("GEMINI_API_KEY"),
)

# Kimi (Moonshot AI) is OpenAI-compatible. Use the correct API base URL:
#   International: https://api.moonshot.ai/v1
#   China:        https://api.moonshot.cn/v1
kimi_client = OpenAI(
    api_key=require_key("KIMI_API_KEY"),
    base_url="https://api.moonshot.ai/v1",
)

# Run with: python api.py