from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    url: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="BOT_CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="allow",
    )

    bot_token: str
    admins: list[int]
    db: DatabaseSettings


settings = Settings()
