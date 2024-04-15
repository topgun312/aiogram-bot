from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot) -> None:
    """
    Функция для установки стандартных команд бота.
    """
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Запустить бота"),
            BotCommand(command="help", description="Вывести справку"),
        ],
        BotCommandScopeDefault(),
    )
