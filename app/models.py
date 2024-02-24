from flask_sqlalchemy import create_engine, ForeignKey
from flask_sqlalchemy import Column, Date, Integer, String
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from appmodule import app


bcrypt = Bcrypt(app)


db = SQLAlchemy()

class User(db.Model):
    username = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String)
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash('password').decode('utf-8') 

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, 'password')







    






