import bson
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDB(object):
    """
    Класс для взаимодействия с клиентом MongoDB
    create_database(self) - создаем БД и загружаем в нее данные из файла sample_collection.bson
    delete_database(self) - удаляем данные из БД
    """

    def __init__(
        self,
        host: str = "localhost",
        port: int = 27017,
        db_name: str = None,
        collection: str = None,
    ):
        self.client = AsyncIOMotorClient(f"mongodb://{host}:{port}")
        self.collection = self.client[db_name][collection]

    async def create_database(self):
        try:
            bson_file = open("sample_collection.bson", "rb")
            bson_data = bson.decode_all(bson_file.read())
            await self.collection.insert_many(bson_data)
        except Exception as ex:
            print("Ошибка: " + str(ex))

    async def delete_database(self):
        await self.client.drop_database(self.client["db_name"])
