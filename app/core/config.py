from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Expected configuration and their types
    app_name: str = "Sentiment Analyzer API with FastAPI"
    debug: bool = True

    class Config:  # Actual configuration file
        env_file = ".env"


settings = Settings()  # Instance Creating
