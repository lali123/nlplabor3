from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str = "bert-base-uncased"
    BATCH_SIZE: int = 16
    LEARNING_RATE: float = 2e-5
    MAX_LENGTH: int = 128
    
    class Config:
        env_file = ".env"

config = Settings()
