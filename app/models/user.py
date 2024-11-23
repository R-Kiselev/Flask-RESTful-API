from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from app.extensions import db, pwd_context
from .user_role import UserRole 


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False, unique = True)
    _password = db.Column("password", db.String(255), nullable = False)

    roles = relationship('Role', secondary = 'user_roles', back_populates = 'users', lazy = True)


    def __init__(self, email, password, roles, **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.roles.extend(roles)

    @hybrid_property
    def password(self, value):
        return self._password

    @password.setter
    def password(self, value):
        self._password = pwd_context.hash(value)