from flask import Blueprint, jsonify
from flask_restful import Api, abort
from marshmallow import ValidationError

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint)

# Banks
from app.api.resources.banks import BankObjectRes, BankListRes
api.add_resource(BankListRes, '/banks')
api.add_resource(BankObjectRes, '/banks/<int:id>')

# Cities
from app.api.resources.cities import CityObjectRes, CityListRes
api.add_resource(CityListRes, '/cities')
api.add_resource(CityObjectRes, '/cities/<int:id>')

# Social statuses
from app.api.resources.social_statuses import SocialStatusObjectRes, SocialStatusListRes
api.add_resource(SocialStatusListRes,'/social-statuses')
api.add_resource(SocialStatusObjectRes,'/social-statuses/<int:id>')

# Clients
from app.api.resources.clients import ClientObjectRes, ClientListRes
api.add_resource(ClientListRes,'/clients')
api.add_resource(ClientObjectRes, '/clients/<int:id>')

# Branches
from app.api.resources.branches import BankBranchObjectRes, BankBranchListRes
api.add_resource(BankBranchListRes,'/banks/<int:bank_id>/branches')
api.add_resource(BankBranchObjectRes,'/banks/branches/<int:id>')

# Accounts
from app.api.resources.accounts import BankAccountObjectRes, BankAccountListRes,\
    ClientAccountObjectRes, ClientAccountListRes
api.add_resource(BankAccountListRes, '/banks/<int:bank_id>/accounts')
api.add_resource(BankAccountObjectRes, '/banks/accounts/<int:id>')
api.add_resource(ClientAccountListRes, '/clients/<int:client_id>/accounts')
api.add_resource(ClientAccountObjectRes, '/clients/<int:client_id>/accounts/<int:account_id>')

# Cards
from app.api.resources.cards import AccountCardObjectRes, AccountCardListRes
api.add_resource(AccountCardListRes, '/accounts/<int:account_id>/cards')
api.add_resource(AccountCardObjectRes, '/accounts/cards/<int:id>')