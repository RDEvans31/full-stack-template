from fastapi import FastAPI
from uuid import uuid4
from typing import Any

app = FastAPI()

@app.get("/")
def hello_world():
    return {
        "status": 200,
        "body": "Hello World"
    }