from db_settings import db
from endpoints.banks.model import Bank
from endpoints.cities.model import City

class Branch(db.Model):
    __tablename__ = 'branches'

    id = db.Column(db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    banks = db.relationship('Bank', backref= 'branch', lazy = True)
    cites = db.relationship('City', backref= 'branch', lazy = True)

    def __repr__(self):
        return f'Id: {self.id}, bank_id: {self.bank_id}, city_id: {self.city_id}'
