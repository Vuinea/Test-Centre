from flask import Blueprint, render_template, request, redirect, url_for
import datetime
from ..forms.teacher_forms import TestForm, StudentTestForm
from ..db.models import Test, Teacher, StudentTest, Student
from ..app import app, db

bp = Blueprint('teacher', __name__, url_prefix='/tests')


@bp.route('/create_test', methods=['GET', 'POST'])
def create_test():
    TEACHER = db.session.query(Teacher).where(Teacher.id == 1).first()
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
    TEACHER = db.session.query(Teacher).where(Teacher.id == 1).first()
    tests = db.session.query(Test).filter(Test.teacher == TEACHER).all()
    return render_template('teacher/tests.html', tests=tests)

@bp.route('/edit/<int:test_id>', methods=['GET', 'POST'])
def edit_test(test_id):
    TEACHER = db.session.query(Teacher).where(Teacher.id == 1).first()
    # Fetch the test by ID and ensure the teacher owns the test
    test = db.session.query(Test).filter(Test.id == test_id, Test.teacher_id == TEACHER.id).first()
    if not test:
        return "Test not found or you do not have permission to edit this test", 404

    enrolled_students = db.session.query(StudentTest).filter(StudentTest.test_id == test_id).all()
    # Create a form instance, pre-populating it with the test's data
    test_form = TestForm(obj=test)

    if request.method == 'POST':
        # Populate the form with the submitted data
        test_form = TestForm(request.form)
        if test_form.validate_on_submit():
            # Update the test's attributes with form data
            test_form.populate_obj(test)
            db.session.commit()
            return redirect(url_for('teacher.get_tests'))
    
    # Creating the student form
    student_form = StudentTestForm()
    # Render the edit form template
    return render_template('teacher/edit_test.html', test_form=test_form, student_form=student_form, test=test, students=enrolled_students)

@bp.route('/delete/<int:test_id>')
def delete_test(test_id):
    TEACHER = db.session.query(Teacher).where(Teacher.id == 1).first()
    test = db.session.query(Test).filter(Test.id == test_id).first()
    if not test:
        return "Test not found", 404

    db.session.delete(test)
    db.session.commit()
    return redirect(url_for('teacher.get_tests'))


@bp.route('/add_student/<int:test_id>', methods=['POST'])
def add_student(test_id):
    TEACHER = db.session.query(Teacher).where(Teacher.id == 1).first()
    test = db.session.query(Test).filter(Test.id == test_id).first()
    if not test:
        return "Test not found", 404
    if request.method == 'POST':
        form = StudentTestForm()
        if form.validate_on_submit():
            student_id = form.student_id.data
            date = form.date.data
            time = form.time.data
            comments = form.comments.data
            date_and_time = datetime.datetime.combine(date, time)
            student = db.session.query(Student).filter(Student.id == student_id).first()
            if not student:
                return "Student not found", 404
            student_test = StudentTest(
                student=student,
                test=test,
                date=date_and_time,
                comments=comments,
            )
            db.session.add(student_test)
            db.session.commit()
            return redirect(url_for('teacher.edit_test', test_id=test_id))

        return redirect(url_for('teacher.edit_test', test_id=test_id))
