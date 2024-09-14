from fastapi import FastAPI
import os
from openai import OpenAI

app = FastAPI()
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

@app.get("/")
async def reach_open_ai_api():
    return completion.choices[0].message.content