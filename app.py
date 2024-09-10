from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import settings as database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = database.SQLALCHEMY_TRACK_MODIFICATIONS

database.db.init_app(app)
api = Api(app)

# Add resources
from endpoints.banks.resource import BanksResource
api.add_resource(BanksResource,'/banks','/banks/<int:bank_id>')

if __name__ == '__main__':
    app.run(debug= True)