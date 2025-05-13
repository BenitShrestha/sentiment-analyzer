from fastapi import APIRouter
from pydantic import BaseModel

from app.services.sentiment import analyze_sentiment

router = APIRouter()


class TextInput(BaseModel):  # Validation
    text: str


@router.post("/analyze")
def analyze_text(input: TextInput):
    result = analyze_sentiment(input.text)
    return result
