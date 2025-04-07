from flask_wtf import FlaskForm
from wtforms.validators import ValidationError
from wtforms import StringField, FloatField, BooleanField, TextAreaField, SubmitField, SelectField
from wtforms.fields import DateField, TimeField
from wtforms.widgets.html5 import DateInput, TimeInput, NumberInput
from wtforms.validators import DataRequired, Optional
import datetime
from ..app import app, db
from ..db.models import Student

with app.app_context():
	students = db.session.query(Student).all()
	student_choices = [(str(student.id), f'{student.preferred} {student.surname}') for student in students]
class TestForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	time = FloatField('Time (minutes)', validators=[DataRequired()], widget=NumberInput(min=0))
	open_note = SelectField('Open Note', choices=[
		(True, 'Yes'),
		(False, 'No')
	],
	coerce=lambda x: x == 'True' if isinstance(x, str) else bool(x))
	comments = TextAreaField('Comments', validators=[Optional()], render_kw={'placeholder': 'Write any test instructions here...'})
	
	def validate_time(self, field):
		if field.data <= 0:
			raise ValidationError('Time must be greater than 0.')
		
class StudentTestForm(FlaskForm):
	# student_id = SelectField('Student', validators=[DataRequired()], 
	# 					 choices=student_choices,
	# 					)
	student_id = StringField('Student', validators=[DataRequired()])
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


