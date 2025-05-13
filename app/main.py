from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Sentiment Analyzer API")

app.include_router(router)


@app.get("/")
def read_root():
    return {"Message": "Welcome to the Sentiment Analyzer API"}
