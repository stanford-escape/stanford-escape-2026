"""
Super simple HTTP server for testing.

Run this with:
uvicorn basic_server:app --reload --host $(ipconfig getifaddr en0) --port 8080

Created by Niklas Vainio on 11/07/2025
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "This is root (on my mac) :O"