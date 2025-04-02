from flask import render_template
from .app import app, db, DB_NAME
from .db.models import *
from .db.database import insert_into_database
import os

db_dir = os.path.join(os.getcwd(), 'instance/test_centre.db')

with app.app_context():
    db.drop_all()
    db.create_all()
    insert_into_database()


@app.route('/')
def home():
    return 'hello world'

@app.route('/test')
def test():
    return render_template('teacher/test_form.html')

from .blueprints.teacher import teacher
app.register_blueprint(teacher)

# flask --app Test-Centre --debug  run

