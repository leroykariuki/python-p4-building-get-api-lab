#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Bakery, BakedGood

fake = Faker()

with app.app_context():
    # Clear existing data
    BakedGood.query.delete()
    Bakery.query.delete()

    bakeries = []
    bakery_names = set()

    # Generate unique bakery names
    while len(bakeries) < 20:
        name = fake.company()
        if name not in bakery_names:
            bakery_names.add(name)
            b = Bakery(name=name)
            bakeries.append(b)

    db.session.add_all(bakeries)

    baked_goods = []
    names = set()

    # Generate unique baked good names
    while len(baked_goods) < 200:
        name = fake.first_name()
        if name not in names:
            names.add(name)
            bg = BakedGood(
                name=name,
                price=randint(1, 10),
                bakery=rc(bakeries)
            )
            baked_goods.append(bg)

    db.session.add_all(baked_goods)

    # Commit the changes to the database
    db.session.commit()

    # Update the price of the most expensive baked good
    most_expensive_baked_good = rc(baked_goods)
    most_expensive_baked_good.price = 100
    db.session.commit()
