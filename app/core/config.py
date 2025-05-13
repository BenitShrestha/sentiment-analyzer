from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Sentiment Analyzer API"
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
