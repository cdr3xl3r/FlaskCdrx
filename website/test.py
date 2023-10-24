#from getopt import error
#from http.client import ACCEPTED
try:
    from flask_login import UserMixin
    print('flask loggin')
except TypeError():
    print('error')
    pass
#from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .__init__ import db


class Base(db.Model):
    pass

class User (Base,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    backup_email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), unique=False)
    portfolio = db.relationship('Portfolio')
    
class Portfolio (Base):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    ledger_name = db.Column(db.String(150), unique=True)
    details= db.Column(db.String(150))
#class Ledger (Base):
    
    








    """    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')"""