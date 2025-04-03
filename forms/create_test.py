from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Optional

class CreateTestForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	time = FloatField('Time', validators=[DataRequired()])
	open_note = BooleanField('Open Note', default=False)
	comments = TextAreaField('Comments', validators=[Optional()])
	