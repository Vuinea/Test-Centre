from sqlalchemy.orm import validates
from ..app import db

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=True)
    preferred = db.Column(db.String(50), nullable=True)
    surname = db.Column(db.String(50), nullable=True)
    TAG_teacher = db.Column(db.String(100), nullable=True)
    block_1 = db.Column(db.String(50), nullable=True)
    block_2 = db.Column(db.String(50), nullable=True)
    block_3 = db.Column(db.String(50), nullable=True)
    block_4 = db.Column(db.String(50), nullable=True)
    block_5 = db.Column(db.String(50), nullable=True)
    block_6 = db.Column(db.String(50), nullable=True)
    block_7 = db.Column(db.String(50), nullable=True)
    block_8 = db.Column(db.String(50), nullable=True)
    diagnosis = db.Column(db.String(255), nullable=True)
    extra_time = db.Column(db.String(50), nullable=True, default='0%')
    room = db.Column(db.Boolean(), default=False)
    computer = db.Column(db.Boolean(), default=False)
    AP_additional_support = db.Column(db.String(255), nullable=True)
    AP_additional_strategies = db.Column(db.String(255), nullable=True)
    overview = db.Column(db.String(255), nullable=True)
    other_concerns = db.Column(db.String(255), nullable=True)
    ELL_extra_time = db.Column(db.String(), default='0%')
    ELL_IB_approved = db.Column(db.Boolean(), default=False)
    dictionary = db.Column(db.Boolean(), nullable=True)
    ELL_additional_notes = db.Column(db.String(255), nullable=True)

    @validates('room', 'computer', 'ELL_IB_approved', 'dictionary')
    def validate_boolean_fields(self, key, value):
        if isinstance(value, str):
            value = value.strip().lower()
            if value == '':
                return False
            elif value == 'yes':
                return True
            elif value == 'no':
                return False
        return value

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    time = db.Column(db.Float, nullable=False)
    open_note = db.Column(db.Boolean, default=False)
    comments = db.Column(db.Text, nullable=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    teacher = db.relationship('Teacher', backref=db.backref('tests', lazy=True))


class StudentTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    deliverd = db.Column(db.Boolean, nullable=False, default=False)

    student = db.relationship('Student', backref=db.backref('student_tests', lazy=True))
    test = db.relationship('Test', backref=db.backref('student_tests', lazy=True))
