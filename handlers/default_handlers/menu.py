import json
from datetime import datetime
from aiogram.types import Message
from database.aggregation_file import get_aggregate_data
from loader import dp


def correct_data(data: str) -> bool:
    """
    Проверка на валидность введенных данных.
    :param data: данные введенные пользователем
    """
    type_list = ["month", "day", "hour"]
    data_dict = json.loads(data)
    time_format = "%Y-%m-%dT%H:%M:%S"
    dt_from = data_dict["dt_from"]
    dt_upto = data_dict["dt_upto"]
    group_type = data_dict["group_type"]
    try:
        res = (
            bool(datetime.strptime(dt_from, time_format))
            and bool(datetime.strptime(dt_upto, time_format))
            and group_type in type_list
        )
    except ValueError:
        res = False
    return res


@dp.message()
async def bot_message(message: Message) -> None:
    try:
        if correct_data(message.text):
            data_dict = json.loads(message.text)
            res = await get_aggregate_data(
                data_dict["dt_from"], data_dict["dt_upto"], data_dict["group_type"]
            )

            await message.answer(res)
        else:
            await message.answer(
                "Невалидный запpос. Пример запроса: \n"
                + '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"} \n'
                + "Параметр group_type должен быть month, day или hour!"
            )
    except:
        await message.answer(
            "Невалидный запpос. Пример запроса: \n"
            + '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"} \n'
            + "Параметр group_type должен быть month, day или hour!"
        )
