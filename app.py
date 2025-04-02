from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
DB_NAME = 'test_centre.db'
db = SQLAlchemy(app)
