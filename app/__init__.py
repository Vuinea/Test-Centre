from flask import render_template
from werkzeug.exceptions import HTTPException
from .app import app, db, DB_NAME
from .db.models import *
from .db.excel_to_database import insert_into_database
import os

db_dir = os.path.join(os.getcwd(), 'instance/test_centre.db')

# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     insert_into_database()
#     t = Teacher(name='John Doe')
#     db.session.add(t)
#     tc_teacher = Teacher(name='Mrs. Slater', test_centre_employee=True)
#     db.session.add(tc_teacher)
#     example_test = Test(name='Example Test', time=60, teacher=t)
#     db.session.add(example_test)
#     db.session.commit()
   

@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return render_template("error/500_generic.html", e=e), 500

@app.errorhandler(404)
def not_found(e):
  return render_template('error/404.html'), 404

from .blueprints.teacher import bp as teacher_bp
app.register_blueprint(teacher_bp)
from .blueprints.test_centre import bp as test_centre_bp
app.register_blueprint(test_centre_bp)

# flask --app app --debug run
# flask --app app run