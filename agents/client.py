from anthropic import Anthropic
from config import (
    ANTHROPIC_API_KEY,
)
client = Anthropic(
    api_key = ANTHROPIC_API_KEY
)

def ask_claude(prompt):
    response = client.messages.create(
        model = "claude-sonnet-4", 
        max_tokens = 1000, 
        messages= {
            "role": "user", 
            "content": prompt
        }
    )
    return response.content[0].text 
