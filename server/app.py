# app.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import models after initializing db
from models import Bakery, BakedGood

# Create tables
with app.app_context():
    db.create_all()

# Routes

@app.route('/bakeries', methods=['GET'])
def bakeries():
    with app.app_context():
        bakeries = Bakery.query.all()
        return jsonify([bakery.serialize() for bakery in bakeries])

@app.route('/bakeries/<int:id>', methods=['GET'])
def bakery_by_id(id):
    bakery = Bakery.query.get_or_404(id)
    return jsonify(bakery.serialize())

@app.route('/baked_goods/by_price', methods=['GET'])
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    return jsonify([baked_good.serialize() for baked_good in baked_goods])

@app.route('/baked_goods/most_expensive', methods=['GET'])
def most_expensive_baked_good():
    baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()
    return jsonify(baked_good.serialize())

if __name__ == '__main__':
    app.run(debug=True)
