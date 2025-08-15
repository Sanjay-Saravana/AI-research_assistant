# backend/main.py
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from crew import run_research_pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/research")
def research_route(topic: str = Body(..., embed=True)):
    result = run_research_pipeline(topic)
    return {"summary": result}