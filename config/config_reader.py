from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс для получения токена из файла .env
    """

    bot_token: SecretStr
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


config = Settings()


DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
)
