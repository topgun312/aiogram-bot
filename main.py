import asyncio
from loguru import logger
import handlers
from database.mongo_db import MongoDB
from loader import bot, dp
from utils.set_bot_commands import set_default_commands


dbase = MongoDB(db_name="company_salaries", collection="salaries")


async def main() -> None:
    """
    Основная функция для запуска бота, удаления и создания данных,
    установки стандартных команд бота
    """
    await dbase.delete_database()
    logger.info("База данных удалена!")
    await dbase.create_database()
    logger.info("База данных создана!")
    await set_default_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.add(
        "logs/logs_{time}.log",
        format="{time} {level} {message}",
        level="DEBUG",
        rotation="08:00",
        compression="zip",
    )
    logger.debug("Error")
    logger.info("Information message")
    logger.warning("Warning")
    asyncio.run(main())
