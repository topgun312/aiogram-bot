from aiogram.filters import Command
from aiogram.types import Message
from loader import dp


@dp.message(Command("start"))
async def bot_start(message: Message) -> None:
    """
    Стартовая функция для начала работы бота.
    """
    await message.answer(f"Привет {message.from_user.first_name}!")


@dp.message(Command("help"))
async def bot_help(message: Message) -> None:
    """
    Функция для работы команды help.
    """
    text = (
        "Пример входных данных: \n"
        + '{"dt_from":"2022-09-01T00:00:00",'
        + '"dt_upto":"2022-12-31T23:59:00",)'
        + '"group_type":"month"} \n'
        + "Комментарий к входным данным:  вы хотите сгруппировать выплаты с 1 сентября 2022 года по 31 декабря 2022 года, по каждому месяцу \n"
        + "Пример ответа: \n"
        + '{"dataset": [5906586, 5515874, 5889803, 6092634], "labels": ["2022-09-01T00:00:00", "2022-10-01T00:00:00", "2022-11-01T00:00:00", "2022-12-01T00:00:00"]} \n'
        + "Комментарий к ответу: в нулевом элементе датасета содержится сумма всех выплат за сентябрь, в первом элементе сумма всех выплат за октябрь и т.д. В лейблах подписи соответственно элементам датасета."
    )
    await message.answer(text=text)
