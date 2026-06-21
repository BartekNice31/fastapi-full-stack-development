import os
from dotenv import load_dotenv
from pathlib import Path

print(Path.cwd())
# env_path=Path("..")/".env"
# print(env_path)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, encoding="utf-8")
load_dotenv(env_path) 
class Settings:
    PROJECT_TITLE = 'Blog🚀'
    PROJECT_VERSION = '0.1.0 🚀'

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    @property
    def SQLALCHEMY_DATABASE_URL(self):
        return (
            f"postgresql://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_SERVER}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )
settings=Settings()