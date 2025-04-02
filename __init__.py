from flask import render_template
from .app import app, db, DB_NAME
from .db.models import *
import os

db_dir = os.path.join(os.getcwd(), 'instance/test_centre.db')

with app.app_context():
    if not os.path.exists(db_dir):
        db.create_all()


@app.route('/')
def home():
    return 'hello world'

@app.route('/test')
def test():
    return render_template('teacher/test_form.html')

from .blueprints.teacher import teacher
app.register_blueprint(teacher)

# flask --app Test-Centre --debug  run

