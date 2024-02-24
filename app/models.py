from flask_sqlalchemy import create_engine, ForeignKey
from flask_sqlalchemy import Column, Date, Integer, String
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from mainappmodule import app
from mainappmodule import login_manager


bcrypt = Bcrypt(app)


db = SQLAlchemy()

class User(db.Model):
    username = db.Column(db.String, primary_key=True, nullable=False)
    password_hash = db.Column(db.String)
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash('password').decode('utf-8') 

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, 'password')
    
    def get_id(self):
        return self.username
    
@login_manager.user_loader
def load_user(username):
    return User.query.get(username)
