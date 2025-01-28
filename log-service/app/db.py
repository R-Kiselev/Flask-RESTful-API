from motor.motor_asyncio import AsyncIOMotorClient
from .config import Config


async def connect_and_init_db():
    global db_client
    try:
        mongodb_uri = Config.app_settings.get('MONGODB_URI')
        db_client = AsyncIOMotorClient(mongodb_uri)
        
        print('Connected to mongo.')
    except Exception as e:
        print(f'Could not connect to mongo: {e}')
        raise


async def get_db_client() -> AsyncIOMotorClient:
    db_name = Config.app_settings.get('DB_NAME')
    return db_client[db_name]


async def close_db_connection():
    global db_client
    if db_client is None:
        print('Connection is None, nothing to close.')
        return
    db_client.close()
    db_client = None
    print('Mongo connection closed.')
