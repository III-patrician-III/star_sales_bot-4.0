from pydantic_settings import BaseSettings

class Config(BaseSettings):
    bot_token: str
    webhook_base: str
    crypto_secret: str
    crypto_project_token: str
    session_string: str
    owner_username: str

cfg = Config(_env_file=".env")
