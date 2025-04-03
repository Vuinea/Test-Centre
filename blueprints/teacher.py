from flask import Blueprint, render_template, request, redirect, url_for
from ..forms.create_test import CreateTestForm
from ..db.models import Test, Teacher
from ..app import app, db

bp = Blueprint('teacher', __name__, url_prefix='/tests')
with app.app_context():
    TEACHER = db.session.query(Teacher).where(Teacher.id == 1).first()


@bp.route('/create_test', methods=['GET', 'POST'])
def create_test():
    form = CreateTestForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Extract form data
        name = form.name.data
        time = form.time.data
        open_note = form.open_note.data
        comments = form.comments.data
        # Create and save the Test object
        test = Test(name=name, time=time, open_note=open_note, comments=comments, teacher=TEACHER)
        db.session.add(test)
        db.session.commit()
    return render_template('teacher/create_test_form.html', form=form)

@bp.route('/')
def get_tests():
    tests = db.session.query(Test).filter(Test.teacher == TEACHER).all()
    return render_template('teacher/tests.html', tests=tests)

