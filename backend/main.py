from fastapi import FastAPI
from pydantic import BaseModel
from nlp import process_text
from strategy import generate_strategy

app = FastAPI()

class UserInput(BaseModel):
    followers: int
    niche: str
    engagement: float
    problem: str

@app.get("/")
def home():
    return {"message": "SocialGrowth AI Backend Running 🚀"}

@app.post("/analyze")
def analyze(data: UserInput):
    keywords = process_text(data.problem)
    strategy = generate_strategy(data, keywords)

    return {
        "keywords": keywords,
        "strategy": strategy
    }