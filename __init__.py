from .app import app, db, DB_NAME
from .db.models import *
from .db.database import insert_into_database
import os

db_dir = os.path.join(os.getcwd(), 'instance/test_centre.db')

# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     insert_into_database()
#     # TODO: remove this
#     t = Teacher(name='John Doe')
#     db.session.add(t)
#     tc_teacher = Teacher(name='Mrs. Slater', test_centre_employee=True)
#     db.session.add(tc_teacher)
#     example_test = Test(name='Example Test', time=60, teacher=t)
#     db.session.add(example_test)
#     db.session.commit()
   

@app.route('/')
def home():
    return 'hello world'

from .blueprints.teacher import bp as teacher_bp
app.register_blueprint(teacher_bp)
from .blueprints.test_centre import bp as test_centre_bp
app.register_blueprint(test_centre_bp)

# flask --app Test-Centre --debug run
