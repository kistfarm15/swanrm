import os

# Sistem akan mencari variabel bernama 'GROQ_API_KEY' di Dashboard Render
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY
)