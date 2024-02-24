from appmodule import app
from app import routes
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.secret_key = "57d208e84bb165bb5c50544a48ecac39bb067f08351d0dd158f7c824f44fca79"

login_manager = LoginManager()
login_manager.init_app(app)
