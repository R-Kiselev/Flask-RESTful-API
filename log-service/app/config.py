import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    '''Custom configuration class for centralizing app settings'''

    app_settings = {
        'DB_NAME': os.getenv('DB_NAME', 'log-service'),
        'MONGODB_URI': os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
    }

    mongodb_collections = {
        'logs': 'logs'
    }

    @classmethod
    def get_collection_name(cls, key: str) -> str:
        if key in cls.mongodb_collections:
            return cls.mongodb_collections[key]
        else:
            raise ValueError(f'Invalid collection name {key}')
