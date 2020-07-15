from datetime import datetime

from app import db


class Owners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer(50))
    city = db.Column(db.String(150))
    data_create = db.Column(db.DateTime, default=datetime.now)
