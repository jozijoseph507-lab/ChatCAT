from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="ChatCAT", description="A fun cat-themed chat API!")

# Request body
class ChatRequest(BaseModel):
    message: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to ChatCAT! Use POST /chat to talk to the cat."}

# Sample cat responses
CAT_RESPONSES = [
    "Meow! 🐱",
    "Purr... I like that! 😺",
    "Hiss! Watch out! 😾",
    "Mrow! Tell me more! 😽",
    "Chirp chirp! 🐾",
    "Zzz... I'm napping now. 💤",
]

# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    user_msg = request.message.strip()
    if not user_msg:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    bot_response = random.choice(CAT_RESPONSES)

    return {"user_message": user_msg, "cat_response": bot_response}
