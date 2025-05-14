from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    description="A Simple API that analyzes sentiment using VADER",
)

app.include_router(router, prefix="/api", tags=["Sentiment"])

"""
Prefix `/api` to make routes distinct: `/api/analyze`
Tags ['Senitment'] groups routes under the ['Sentiment'] category
Also adds a drop down
"""


@app.get("/")
def read_root():
    return {"Message": f"Welcome to the {settings.app_name}"}
