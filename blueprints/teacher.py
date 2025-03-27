from flask import render_template, request
from flask.blueprints import Blueprint
from ..app import db
from ..db.models import Test, Student

teacher = Blueprint('teacher', __name__, url_prefix='/teacher')

@teacher.route('/test_form', methods=['GET', 'POST'])
def create_test():
    context = {}
    if request.method == 'POST':
        pass

    students = Student.query.all()

    return render_template('teacher/test_form.html', students=students, **context)

