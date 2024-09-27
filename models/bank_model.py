from db_settings import db
from models.account_model import Account

class Bank(db.Model):
    __tablename__ = 'banks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    accounts = db.relationship('Account', backref='bank', lazy = 'select')

    def __repr__(self):
        return f'Id: {self.id}, name: {self.name}'
    