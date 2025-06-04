from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./products.db"
    API_KEY: str = "secretkey"

    class Config:
        env_file = ".env"


settings = Settings()
