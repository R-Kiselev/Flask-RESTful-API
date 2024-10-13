from flask import Flask, Blueprint, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import db_settings as database
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = database.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = database.SQLALCHEMY_TRACK_MODIFICATIONS

database.db.init_app(app)
blueprint = Blueprint("api", __name__)

api = Api(blueprint)
ma = Marshmallow(app)

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400

# Add resources
from resources.banks import BankObjectResource, BankListResource
api.add_resource(BankListResource, '/banks')
api.add_resource(BankObjectResource, '/banks/<int:id>')

from resources.cities import CityObjectResource, CityListResource
api.add_resource(CityListResource, '/cities')
api.add_resource(CityObjectResource, '/cities/<int:id>')

from resources.social_statuses import SocialStatusObjectResource, SocialStatusListResource
api.add_resource(SocialStatusListResource,'/social-statuses')
api.add_resource(SocialStatusObjectResource,'/social-statuses/<int:id>')

from resources.clients import ClientObjectResource, ClientListResource
api.add_resource(ClientListResource,'/clients')
api.add_resource(ClientObjectResource, '/clients/<int:id>')

from resources.branches import BranchObjectResource, BranchListResource
#   ,'/banks/<int:id>/branches'
api.add_resource(BranchObjectResource,'/banks/branches/<int:id>')

from resources.accounts import AccountObjectResource, AccountListResource
# #   , '/banks/<int:id>/accounts'
# #   , '/clients/<int:id>/accounts'
# #   , '/clients/<int:id>/accounts/<int:id>'
api.add_resource(AccountObjectResource, '/banks/accounts/<int:id>')

from resources.cards import CardObjectResource, CardListResource
#   , '/accounts/<int:id>/cards'
api.add_resource(CardObjectResource, '/accounts/cards/<int:id>')

app.register_blueprint(blueprint, url_prefix="/api")

if __name__ == '__main__':
    app.debug = False
    app.run(ssl_context = 'adhoc')