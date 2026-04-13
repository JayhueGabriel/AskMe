import anthropic
import os
from dotenv import load_dotenv
from config import MODEL

load_dotenv()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def ask(query):
    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content":query}]
    )
    return message.content[0].text