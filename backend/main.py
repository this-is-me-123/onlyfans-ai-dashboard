from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database
chat_histories = {}

class ChatRequest(BaseModel):
    user_id: str
    model: str
    message: str

@app.get("/users")
def get_users():
    return [
        {"id": "123", "name": "Jane Doe", "joined": "2023-01-01"},
        {"id": "456", "name": "John Smith", "joined": "2024-01-01"},
    ]

@app.get("/analytics")
def get_analytics():
    return {"tips": 1000, "messages": 42}

@app.post("/chat")
def chat(request: ChatRequest):
    reply = f"[{request.model}]: I received your message - '{request.message}'."
    history = chat_histories.setdefault(request.user_id, [])
    history.append({"from": "user", "text": request.message})
    history.append({"from": request.model, "text": reply})
    return {"reply": reply}

@app.get("/history/{user_id}")
def get_history(user_id: str):
    return chat_histories.get(user_id, [])

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
