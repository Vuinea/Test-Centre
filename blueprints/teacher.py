from flask import Blueprint, render_template, request, redirect, url_for
from ..forms.test import TestForm
from ..db.models import Test, Teacher
from ..app import app, db

bp = Blueprint('teacher', __name__, url_prefix='/tests')
with app.app_context():
    TEACHER = db.session.query(Teacher).where(Teacher.id == 1).first()


@bp.route('/create_test', methods=['GET', 'POST'])
def create_test():
    form = TestForm()
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
    return render_template('teacher/create_test.html', form=form)

@bp.route('/')
def get_tests():
    tests = db.session.query(Test).filter(Test.teacher == TEACHER).all()
    return render_template('teacher/tests.html', tests=tests)

@bp.route('/edit/<int:test_id>', methods=['GET', 'POST'])
def edit_test(test_id):
    # Fetch the test by ID and ensure the teacher owns the test
    test = db.session.query(Test).filter(Test.id == test_id, Test.teacher_id == TEACHER.id).first()
    if not test:
        return "Test not found or you do not have permission to edit this test", 404

    # Create a form instance, pre-populating it with the test's data
    form = TestForm(obj=test)

    if request.method == 'POST':
        # Populate the form with the submitted data
        form = TestForm(request.form)
        if form.validate_on_submit():
            # Update the test's attributes with form data
            form.populate_obj(test)
            db.session.commit()
            return redirect(url_for('teacher.get_tests'))    
    # Render the edit form template
    return render_template('teacher/edit_test.html', form=form, test=test)

@bp.route('/delete/<int:test_id>')
def delete_test(test_id):
    test = db.session.query(Test).filter(Test.id == test_id).first()
    if not test:
        return "Test not found", 404

    db.session.delete(test)
    db.session.commit()
    return redirect(url_for('teacher.get_tests'))


