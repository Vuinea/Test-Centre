from flask import render_template
from .app import app, db


@app.route('/')
def home():
    return 'hello world'

@app.route('/test')
def test():
    return render_template('teacher/test_form.html')

from .blueprints.teacher import teacher
app.register_blueprint(teacher)

# flask --app Test-Centre --debug  run

