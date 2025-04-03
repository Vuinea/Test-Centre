from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
DB_NAME = 'test_centre.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
# TODO: Set a random key for app
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
