from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/analytics")
def get_analytics():
    return {"tips": 1000, "messages": 42}

@app.get("/users")
def get_users():
    return [
        {"id": "123", "name": "Jane Doe", "joined": "2023-01-01"},
        {"id": "456", "name": "John Smith", "joined": "2024-01-01"},
    ]

@app.post("/chat")
async def chat(payload: dict):
    message = payload.get("message", "")
    model = payload.get("model", "Lana")
    reply = f"[{model}]: I received your message - '{message}'."
    return {"reply": reply}

@app.get("/history/{user_id}")
def get_history(user_id: str):
    return [
        {"user": "Hello", "model": "Hi there!", "timestamp": "2023-01-01T12:00:00Z"},
        {"user": "How are you?", "model": "I'm great, thanks!", "timestamp": "2023-01-01T12:05:00Z"}
    ]

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
