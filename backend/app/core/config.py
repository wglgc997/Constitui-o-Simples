
from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Aplicacao
    APP_NAME: str = "Constituicao Simples"
    APP_ENV: Literal["development", "testing", "production"] = "development"
    DEBUG: bool = False

    # Banco de dados
    DATABASE_URL: str

    # Frontend
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]

    # Inteligencia Artificial
    LLM_PROVIDER: str = "openrouter"
    LLM_BASE_URL: str = "https://openrouter.ai/api/v1"
    LLM_API_KEY: str = ""
    LLM_MODEL: str = ""

    # Geracao antecipada
    AI_GENERATION_ENABLED: bool = True
    AI_REVIEW_ENABLED: bool = True
    AI_BATCH_SIZE: int = 5
    AI_MAX_RETRIES: int = 3

    # Publicacao
    AUTO_PUBLISH_AI_CONTENT: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
