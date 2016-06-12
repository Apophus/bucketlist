#!usr/bin/python

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.column(db.String(64), index=True, unique =True)
    email = db.column(db.String(120), index = True, unique = True)
    
    #tells python how to print objects of this class
    def __repr__(self):
        return '<User %r>' %(self.nickname)
