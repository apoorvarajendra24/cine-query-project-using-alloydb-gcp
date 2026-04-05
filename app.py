from fastapi import FastAPI
from adk_agent.root_agent import root_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CineQuery Agent is running 🎬"}

@app.get("/query")
def query(q: str):
    return root_agent(q)
