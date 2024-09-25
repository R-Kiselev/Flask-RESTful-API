from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import db_settings as database

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = database.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = database.SQLALCHEMY_TRACK_MODIFICATIONS

database.db.init_app(app)
api = Api(app)

# Add resources
from endpoints.banks.resource import BankResource
api.add_resource(BankResource,'/banks','/banks/<int:id>')

from endpoints.cities.resource import CityResource
api.add_resource(CityResource,'/cities','/cities/<int:id>')

from endpoints.branches.resource import BranchResource
api.add_resource(BranchResource,'/branches','/branches/<int:id>')

from endpoints.social_statuses.resource import SocialStatusResource
api.add_resource(SocialStatusResource,'/social_statuses','/social_statuses/<int:id>')

from endpoints.clients.resource import ClientResource
api.add_resource(ClientResource,'/clients','/clients/<int:id>')

from endpoints.accounts.resource import AccountResource
api.add_resource(AccountResource, '/accounts', '/accounts/<int:id>')

from endpoints.cards.resource import CardResource
api.add_resource(CardResource, '/cards', '/cards/<int:id>')

if __name__ == '__main__':
    app.debug = False
    app.run(ssl_context = 'adhoc')