from environs import Env
from pydantic import BaseSettings, Field, validator

env = Env()
env.read_env()

class Settings(BaseSettings):
    """Класс настроек проекта"""
    APP_PORT: int
    PYTHONPATH: str


setting = Settings()