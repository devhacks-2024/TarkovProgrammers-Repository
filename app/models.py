from flask_sqlalchemy import create_engine, ForeignKey
from flask_sqlalchemy import Column, Date, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    username = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String)



    






