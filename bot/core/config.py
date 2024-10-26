from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Bot configuration"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="BOT_CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    bot_token: str


settings = Settings()
