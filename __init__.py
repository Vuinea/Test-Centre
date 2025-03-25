from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test_centre.db"
db = SQLAlchemy(app)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ms_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)
    extra_time = db.Column(db.Float, nullable=True)
    accommodations = db.Column(db.Text, nullable=True)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    time = db.Column(db.Float, nullable=False)
    open_note = db.Column(db.Boolean, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    teacher = db.relationship('Teacher', backref=db.backref('tests', lazy=True))


class StudentTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    comments = db.Column(db.Text, nullable=True)

    student = db.relationship('Student', backref=db.backref('student_tests', lazy=True))
    test = db.relationship('Test', backref=db.backref('student_tests', lazy=True))


@app.route('/')
def home():
    return 'hello world'

@app.route('/test')
def test():
    return render_template('teacher/test_form.html')
