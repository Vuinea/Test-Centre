from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test_centre.db"
db = SQLAlchemy(app)


@app.route('/')
def home():
    return 'hello world'

@app.route('/test')
def test():
    return render_template('teacher/test_form.html')
