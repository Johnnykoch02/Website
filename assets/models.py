from enum import unique
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(72), unique=True )
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(60))  
    notes = db.relationship('Note')
    groups = db.relationship('Group')

class Group(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    group_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(72), unique=False)
    phone_number = db.Column(db.String(15), unique=False)
    drivers_license = db.Column(db.String(20), unique=False)
    email_address = db.Column(db.String(72), unique=False)
    time_started = db.Column(db.DateTime(timezone=True), default=func.now())
    consent = db.Column(db.String(72), unique=False)
    active = db.Column(db.Boolean)
