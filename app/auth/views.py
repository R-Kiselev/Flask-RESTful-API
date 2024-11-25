from flask import (
    Blueprint,
    jsonify,
    request
)
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_current_user,
    get_jwt
)

from app.extensions import jwt, pwd_context
from app.api.resources.users import UserListResource
from app.models.user import User

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/register', methods = ['POST'])
def register():
    try:
        response = UserListResource().post()
        return response
    except Exception as e:
        return jsonify({"error" : str(e)}), 400


@blueprint.route('/login', methods = ['POST'])
def login():
    req = request.json
    email = req.get('email', None)
    password = req.get('password', None)

    if not email or not password:
        return jsonify({'msg' : 'Missing required fields'}), 400

    user = User.query.filter_by(email = email).first()
    if user is None or not pwd_context.verify(password, user.password):
        return jsonify({'msg' : 'Bad credentials'}), 400
    
    access_token = create_access_token(identity=user.id)

    return jsonify({'access_token' : access_token}), 200


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_payload):
    identity = jwt_payload["sub"]
    return User.query.get(identity)


@blueprint.route('/whoami', methods = ['GET'])
@jwt_required()
def whoami():
    current_user = get_current_user()
    return jsonify({
        'email' : current_user.email,
        'roles' : [role.name for role in current_user.roles]
    })