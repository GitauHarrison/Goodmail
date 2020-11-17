from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    site_url = db.Column(db.String(128), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) 
    
    def __repr__(self):
        return 'User <>'.format(self.email)