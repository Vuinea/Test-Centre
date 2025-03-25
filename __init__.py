from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

@app.route('/test')
def test():
    return render_template('teacher/test_form.html')
