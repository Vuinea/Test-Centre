from flask import Blueprint, render_template, request
from ..forms.create_test import CreateTestForm
from ..db.models import Test, Teacher
from ..app import db

bp = Blueprint('teacher', __name__)


@bp.route('/create_test', methods=['GET', 'POST'])
def create_test():
    form = CreateTestForm()
    teacher = db.session.query(Teacher).where(Teacher.id == 1).first()
    if request.method == 'POST' and form.validate_on_submit():
        # Extract form data
        name = form.name.data
        time = form.time.data
        open_note = form.open_note.data
        comments = form.comments.data
        # Create and save the Test object
        test = Test(name=name, time=time, open_note=open_note, comments=comments, teacher=teacher)
        db.session.add(test)
        db.session.commit()
    return render_template('teacher/create_test_form.html', form=form)

