import os

from dotenv import load_dotenv

load_dotenv()

FLASK_RUN_CERT = os.getenv("FLASK_CERT")
ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == 'development'
SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False