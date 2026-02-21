from fastapi import FastAPI
from pydantic import BaseModel
from .preprocessor import TextCleaner

app = FastAPI(title="NLP Inference Service")
cleaner = TextCleaner()

class InferenceRequest(BaseModel):
    text: str

@app.post("/predict")
async def predict(request: InferenceRequest):
    cleaned_text = cleaner.clean(request.text)
    # Logic for model inference would go here
    return {"input": request.text, "cleaned": cleaned_text, "label": "positive"}
