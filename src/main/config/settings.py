from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: str = "DEBUG"
    API_COIN_BASE_BASE_URL: str = ""
    NOTIFICATION_CLIENT_URL: str = ""
    NOTIFICATION_RECIPIENT_ID: str = ""

    class Config:
        env_file = ".env"
        env_file_encode = "utf-8"


settings = Settings()
