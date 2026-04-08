import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "MAIL AI AGENT"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./mail_agent.db")
    HUEY_DB_URL: str = os.getenv("HUEY_DB_URL", "huey_queue.db")
    APP_URL: str = os.getenv("APP_URL", "http://localhost:5173")
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
    SMTP_HOST: str = os.getenv("SMTP_HOST", "localhost")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASS: str = os.getenv("SMTP_PASS", "")

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
