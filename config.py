from dotenv import load_dotenv
import os

load_dotenv("env/.env.local")

ANTHROPIC_API_KEY = os.getenv(
    "ANTHROPIC_API_KEY"
)

JWT_SECRET = os.getenv(
    "JWT_SECRET"
)