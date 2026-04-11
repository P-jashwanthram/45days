from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI("YOUR_API_KEY")

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(msg: Message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": msg.text}
        ]
    )
    return {"reply": response.choices[0].message.content}