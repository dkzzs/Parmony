from . import db
from datetime import datetime
import matplotlib.pyplot as plt


class Carpark(db.Model):
    __tablename__ = 'carparks'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    code = db.Column(db.String(64),unique=True, nullable=False)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text())
    city = db.Column(db.String(64), nullable=False)
    address = db.Column(db.Text(), nullable=False)
    num_of_space = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(64))
    longtitude = db.Column(db.Float())
    latitude = db.Column(db.Float())
    demand = db.Column(db.String(64))
    created_timestamp = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    last_updated_timestamp = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    transactions = db.relationship('Transaction', backref='carpark', lazy='dynamic')

    def gen_volume_chart(self):
        pass


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    entry_timestamp = db.Column(db.DateTime(), nullable=False)
    exit_timestamp = db.Column(db.DateTime(), nullable=False)
    tx_timestamp = db.Column(db.DateTime(), nullable=False)
    parker_type = db.Column(db.String(64), nullable=False)
    license = db.Column(db.String(64))
    gross_price = db.Column(db.Float())
    validation = db.Column(db.Float())
    validation_type = db.Column(db.String(64))
    net_price = db.Column(db.Float())
    payment_method = db.Column(db.String(64))
    payment_location = db.Column(db.String(64))
    entry_gate = db.Column(db.String(64))
    exit_gate = db.Column(db.String(64))
    operator = db.Column(db.String(64))
    length_of_stay = db.Column(db.Float(), nullable=False)
    length_of_stay_until_pay = db.Column(db.Float(), nullable=False)
    created_timestamp = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    last_updated_timestamp = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    carpark_id = db.Column(db.Integer, db.ForeignKey('carparks.id'))

    @property
    def los(self):
        return self.exit_timestamp - self.entry_timestamp

