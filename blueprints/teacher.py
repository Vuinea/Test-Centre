from flask import Blueprint

teacher = Blueprint('teacher', __name__)


@teacher.route('/create_form')
def create_form():
    return 'create form'
