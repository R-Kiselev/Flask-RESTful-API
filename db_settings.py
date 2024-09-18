from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Change SQLALCHEMY_DATABASE_URI according to the template below
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/database'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@localhost/mybank'
SQLALCHEMY_TRACK_MODIFICATIONS = False