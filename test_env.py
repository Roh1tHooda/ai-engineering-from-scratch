import os
from dotenv import load_dotenv

load_dotenv()

anthropic_key = os.getenv("ANTHROPIC_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

print("Anthropic key loaded:", bool(anthropic_key))
print("OpenAI key loaded:", bool(openai_key))
