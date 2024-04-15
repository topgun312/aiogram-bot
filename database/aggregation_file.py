import json
from datetime import datetime
from main import dbase


async def get_aggregate_data(dt_from: str, dt_upto: str, group_type: str) -> str:
    """
    Функция для агрегации статистических данных о зарплатах сотрудников компании по временным промежуткам
    :param dt_from: - Дата и время старта агрегации в ISO формате
    :param dt_upto: - Дата и время окончания агрегации в ISO формате
    :param group_type: - Тип агрегации
    """
    global date_format
    if group_type == "hour":
        date_format = "%Y-%m-%dT%H:00:00"
    elif group_type == "day":
        date_format = "%Y-%m-%dT00:00:00"
    elif group_type == "month":
        date_format = "%Y-%m-01T00:00:00"

    pipeline = [
        {
            "$match": {
                "dt": {
                    "$gte": datetime.fromisoformat(dt_from),
                    "$lte": datetime.fromisoformat(dt_upto),
                }
            }
        },
        {
            "$group": {
                "_id": {
                    "$dateToString": {"format": date_format, "date": {"$toDate": "$dt"}}
                },
                "total_salaries": {"$sum": "$value"},
            }
        },
        {"$sort": {"_id": 1}},
    ]

    result = await dbase.collection.aggregate(pipeline=pipeline).to_list(length=None)
    dataset = [res["total_salaries"] for res in result]
    labels = [res["_id"] for res in result]

    return json.dumps({"dataset": dataset, "labels": labels})
