from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    user_salt = db.Column(db.String(50))
    password_salt = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)