from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import db_settings as database
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = database.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = database.SQLALCHEMY_TRACK_MODIFICATIONS

database.db.init_app(app)
api = Api(app)
ma = Marshmallow(app)

'''

Филиалы банка:

GET /banks/branches/{id} — получить информацию о конкретном филиале.
GET /banks/{id}/branches — получить список филиалов конкретного банка.

Счета:

GET /banks/accounts/{id} — получить информацию о конкретном счете.
GET /banks/{id}/accounts — получить все счета банка.

GET /clients/{id}/accounts — получить список счетов конкретного клиента.
GET /clients/{id}/accounts/{id} — получить счет конкретного клиента.

Карты:

GET /accounts/cards/{id} — получить список карт для конкретного счета.
GET /accounts/{id}/cards — получить список карт для конкретного счета.


Советы:
1) Создание кстати хорошо сделать через /banks/id/accounts
2) Главное логику вынести в сервис, чтобы не дублировать код
3) Использовать marshmallow вместо reqparser  
'''

# Add resources
from resources.banks import BankResource
api.add_resource(BankResource,'/banks','/banks/<int:id>')

from resources.cities import CityResource
api.add_resource(CityResource,'/cities','/cities/<int:id>')

from resources.social_statuses import SocialStatusResource
api.add_resource(SocialStatusResource,'/social_statuses','/social-statuses/<int:id>')

from resources.clients import ClientResource
api.add_resource(ClientResource,'/clients','/clients/<int:id>')



from resources.branches import BranchResource
#   ,'/banks/<int:id>/branches'
api.add_resource(BranchResource,'/banks/branches/<int:id>')

from resources.accounts import AccountResource
#   , '/banks/<int:id>/accounts'
#   , '/clients/<int:id>/accounts'
#   , '/clients/<int:id>/accounts/<int:id>'
api.add_resource(AccountResource, '/banks/accounts/<int:id>')

from resources.cards import CardResource
#   , '/accounts/<int:id>/cards'
api.add_resource(CardResource, '/accounts/cards/<int:id>')

if __name__ == '__main__':
    app.debug = False
    app.run(ssl_context = 'adhoc')