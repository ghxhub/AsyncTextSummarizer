# project/app/config.py


import logging
from functools import lru_cache
# from pydantic_settings import BaseSettings
from pydantic import BaseSettings
import os

log = logging.getLogger("uvicorn")


# class Settings(BaseSettings):
#     environment: str = "dev"
#     testing: bool = bool(0)

class Settings(BaseSettings):
    environment: str = os.getenv('ENVIRONMENT', 'dev')
    testing: bool = os.getenv('TESTING', '0')

@lru_cache
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
