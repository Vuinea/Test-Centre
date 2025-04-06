from flask import Blueprint, render_template, request, redirect, url_for
from ..db.models import Teacher, Test, StudentTest
from ..app import db

bp = Blueprint('test_centre', __name__, url_prefix='/test_centre')


@bp.route('/')
def view_schedule():
    TEACHER = db.session.query(Teacher).where(Teacher.id == 2).first()
    # checking if they have permission to access the page
    if not TEACHER.test_centre_employee:
        return "You do not have permission to access this page", 403
    
    # Get all of the tests
    tests = db.session.query(StudentTest).all()
    
    return render_template('test_centre/view_schedule.html', tests=tests)


@bp.route('view_student_test/<int:student_test_id>')
def view_student_test(student_test_id: int):
    TEACHER = db.session.query(Teacher).where(Teacher.id == 2).first()
    # checking if they have permission to access the page
    if not TEACHER.test_centre_employee:
        return "You do not have permission to access this page", 403
    
    # Get the test
    student_test = db.session.query(StudentTest).where(StudentTest.id == student_test_id).first()
    if not student_test:
        return "Student test not found", 404
    student = student_test.student
    print(student_test)
    yes_no = {
        True: "Yes",
        False: "No"
    }
    student_info = {
        'Full Name': student.first_name + " " + student.surname,
        'Room': yes_no[student.room],
        'Computer': yes_no[student.computer],
        'AP_Additional_Support': student.AP_additional_support,
        'AP_Additional_Strategies': student.AP_additional_strategies,
        'Overview': student.overview,
        'ELL IB Approved': yes_no[student.ELL_IB_approved],
        'Dictionary': yes_no[student.dictionary],
        'ELL Additional Notes': student.ELL_additional_notes,
        'ELL Extra Time': f'{int(student.ELL_extra_time * 100)}%',
        'AP Extra Time': f'{int(student.extra_time * 100)}%',
        # 'total_time': student_test.test.time + student.extra_time * student_test.test.time + student.ell_extra_time * student_test.test.time,

    }

    test = student_test.test
    test_info = {
        'Name': test.name,
        'Date': f'{student_test.date.date()} at {student_test.date.time()}',
        'Duration (minutes)': test.time + test.time * student.extra_time + test.time * student.ELL_extra_time,
        'Open Note': yes_no[test.open_note],
        'Student Comments': student_test.comments,
        'Test Comments': test.comments,
        'Delivered': student_test.delivered,
        'Teacher': test.teacher.name,
    }


    return render_template('test_centre/view_student_test.html', 
                           student_test=student_test,
                           student_info=student_info,
                           test_info=test_info
                           )
