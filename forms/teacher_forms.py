from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, TextAreaField, SubmitField, SelectField
from wtforms.fields import DateField, TimeField
from wtforms.widgets.html5 import DateInput, TimeInput
from wtforms.validators import DataRequired, Optional
from wtforms.widgets import Select
import datetime
from ..app import app, db
from ..db.models import Student

with app.app_context():
	students = db.session.query(Student).all()
	student_choices = [(str(student.id), f'{student.preferred} {student.surname}') for student in students]
class TestForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	time = FloatField('Time', validators=[DataRequired()])
	open_note = BooleanField('Open Note', default=False)
	comments = TextAreaField('Comments', validators=[Optional()])

class StudentTestForm(FlaskForm):
	student_id = SelectField('Student', validators=[DataRequired()], 
						 choices=student_choices,
						)
	date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()], widget=DateInput(),
				  render_kw={
                                          'min': datetime.datetime.now().strftime("%Y-%m-%d")
				  })
	time = TimeField('Time', validators=[DataRequired()], widget=TimeInput(),
				  render_kw={
										  'min': datetime.time(hour=8, minute=15),
										  'max': datetime.time(hour=17, minute=30),
				  })
	comments = TextAreaField('Comments', validators=[Optional()])
	submit = SubmitField('Submit')

	def iter_choices(self):
		# This method is used to iterate over the choices for the student_id field
		return student_choices


