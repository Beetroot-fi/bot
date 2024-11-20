from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class RedisConfig(BaseModel):
    """Redis configuration"""

    host: str
    port: int
    decode_responses: bool = True


class Settings(BaseSettings):
    """Bot configuration"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="BOT_CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    bot_token: str
    admins: list[int]
    redis: RedisConfig


settings = Settings()
