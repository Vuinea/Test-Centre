from sqlalchemy.orm import validates
from ..app import db

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    test_centre_employee = db.Column(db.Boolean, default=False)

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
    extra_time = db.Column(db.Float(), default=0)
    room = db.Column(db.Boolean(), default=False)
    computer = db.Column(db.Boolean(), default=False)
    AP_additional_support = db.Column(db.String(255), nullable=True)
    AP_additional_strategies = db.Column(db.String(255), nullable=True)
    overview = db.Column(db.String(255), nullable=True)
    other_concerns = db.Column(db.String(255), nullable=True)
    ELL_extra_time = db.Column(db.Float(), default=0)
    ELL_IB_approved = db.Column(db.Boolean(), default=False)
    dictionary = db.Column(db.Boolean(), nullable=True)
    ELL_additional_notes = db.Column(db.String(255), nullable=True)

    @validates('room', 'computer', 'ELL_IB_approved', 'dictionary')
    def validate_boolean_fields(self, key, value):
        if isinstance(value, str):
            value = value.strip().lower()
            if value == '':
                return False
            if value == 'yes':
                return True
            return False
        return value

    @validates('extra_time', 'ELL_extra_time')
    def validate_time_fields(self, key, value):
        if isinstance(value, str):
            value = value.strip()
            if value == '':
                return 0.0
            elif '%' in value:
                try:
                    return float(value.replace('%', '').strip()) / 100
                except ValueError:
                    raise ValueError(f"Invalid percentage format for {key}: {value}")
            else:
                try:
                    return float(value)
                except ValueError:
                    raise ValueError(f"Invalid float format for {key}: {value}")
        elif isinstance(value, (int, float)):
            return float(value)
        else:
            raise ValueError(f"Invalid type for {key}: {type(value)}")


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    time = db.Column(db.Float, nullable=False)
    open_note = db.Column(db.Boolean, default=False)
    comments = db.Column(db.Text, nullable=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    teacher = db.relationship('Teacher', backref=db.backref('tests', lazy=True))

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Name cannot be empty")
        return value.strip().lower()


class StudentTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    delivered = db.Column(db.Boolean, nullable=False, default=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    student = db.relationship('Student', backref=db.backref('student_tests', lazy=True))
    test = db.relationship('Test', backref=db.backref('student_tests', lazy=True))
