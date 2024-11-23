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
from app.api.resources.branches import BranchObjectRes, BranchListRes
api.add_resource(BranchListRes,'/banks/<int:bank_id>/branches')
api.add_resource(BranchObjectRes,'/branches/<int:id>')

# Accounts
from app.api.resources.accounts import AccountObjectRes, BankAccountListRes,\
    ClientAccountListRes
api.add_resource(BankAccountListRes, '/banks/<int:bank_id>/accounts')
api.add_resource(ClientAccountListRes, '/clients/<int:client_id>/accounts')
api.add_resource(AccountObjectRes, '/accounts/<int:id>')

# Cards
from app.api.resources.cards import CardObjectRes, AccountCardListRes
api.add_resource(AccountCardListRes, '/accounts/<int:account_id>/cards')
api.add_resource(CardObjectRes, '/cards/<int:id>')


# Users
from app.api.resources.users import UserObjectResource, UserListResource
api.add_resource(UserListResource, '/users')
api.add_resource(UserObjectResource, '/users/<int:id>')


# Roles
from app.api.resources.roles import RoleObjectRes, RoleListRes
api.add_resource(RoleListRes, '/users/roles')
api.add_resource(RoleObjectRes, '/users/roles/<int:id>')