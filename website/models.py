from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    ledger_name = db.Column(db.String(150), unique=True)
    details = db.Column(db.String(150))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    backup_email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), unique=False)
    enabled_user = db.Column(db.Boolean, default=True)
    portfolio = db.relationship("Portfolio")
