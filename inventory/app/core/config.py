from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./inventory.db"
    PRODUCTS_SERVICE_URL: str = "http://products:8001"
    API_KEY: str = "supersecretkey"

    class Config:
        env_file = ".env"

settings = Settings()
