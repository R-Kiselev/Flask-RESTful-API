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
from resources.banks import BankObjectRes, BankListRes
api.add_resource(BankListRes, '/banks')
api.add_resource(BankObjectRes, '/banks/<int:id>')

from resources.cities import CityObjectRes, CityListRes
api.add_resource(CityListRes, '/cities')
api.add_resource(CityObjectRes, '/cities/<int:id>')

from resources.social_statuses import SocialStatusObjectRes, SocialStatusListRes
api.add_resource(SocialStatusListRes,'/social-statuses')
api.add_resource(SocialStatusObjectRes,'/social-statuses/<int:id>')

from resources.clients import ClientObjectRes, ClientListRes
api.add_resource(ClientListRes,'/clients')
api.add_resource(ClientObjectRes, '/clients/<int:id>')

from resources.branches import BankBranchObjectRes, BankBranchListRes
api.add_resource(BankBranchListRes,'/banks/<int:bank_id>/branches')
api.add_resource(BankBranchObjectRes,'/banks/branches/<int:id>')

from resources.accounts import BankAccountObjectRes, ClientAccountListRes, ClientAccountObjectRes, BankAccountListRes
api.add_resource(BankAccountObjectRes, '/banks/accounts/<int:id>')
api.add_resource(BankAccountListRes, '/banks/<int:bank_id>/accounts')
api.add_resource(ClientAccountListRes, '/clients/<int:client_id>/accounts')
api.add_resource(ClientAccountObjectRes, '/clients/<int:client_id>/accounts/<int:account_id>')

from resources.cards import AccountCardObjectRes, AccountCardListRes
api.add_resource(AccountCardListRes, '/accounts/<int:account_id>/cards')
api.add_resource(AccountCardObjectRes, '/accounts/cards/<int:id>')

app.register_blueprint(blueprint, url_prefix="/api")

if __name__ == '__main__':
    app.debug = False
    app.run(ssl_context = 'adhoc')