from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@localhost/mybank'
SQLALCHEMY_TRACK_MODIFICATIONS = False