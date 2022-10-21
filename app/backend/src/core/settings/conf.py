import os
import sys

from environs import Env
from pydantic import BaseSettings

env = Env()
env.read_env()

if not os.environ.get("PYTHONPATH"):
    os.environ["PYTHONPATH"] = sys.path[0]


class Settings(BaseSettings):
    """Класс настроек проекта"""
    APP_PORT: int
    PYTHONPATH: str


setting = Settings()
