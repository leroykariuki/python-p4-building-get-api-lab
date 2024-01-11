# models.py
from app import db

class Bakery(db.Model):
    __tablename__ = 'bakery'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class BakedGood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
