from functools import wraps

from flask import jsonify, make_response
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_current_user
)

from app.models.role import Role


def user_roles_required(*required_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            current_user = get_current_user()

            if not any(role.name in required_roles for role in current_user.roles):
                return make_response(jsonify({'error': 'Access denied'}), 403)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator