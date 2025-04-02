from flask import render_template
from .app import app, db, DB_NAME
from .db.models import *
from .db.database import load_data_from_excel, merge_data
import os

db_dir = os.path.join(os.getcwd(), 'instance/test_centre.db')

with app.app_context():
    if not os.path.exists(db_dir):
        db.drop_all()
    
    db.create_all()
    data = load_data_from_excel('instance/ap_ell_master_for_teachers.xlsx')
    merged = merge_data(*data)
    records = merged.to_dict(orient="records")
    # students = [Student(**record) for record in records]
    # db.session.bulk_save_objects(students)
    # db.session.commit()

    for _, row in merged.iterrows():
        student_dict = {
            'first_name': row['First Name'],
            'preferred': row['Preferred'],
            'surname': row['Surname'],
            'TAG_teacher': row['TAG Teacher'],
            'block_1': row['Block 1'],
            'block_2': row['Block 2'],
            'block_3': row['Block 3'],
            'block_4': row['Block 4'],
            'block_5': row['Block 5'],
            'block_6': row['Block 6'],
            'block_7': row['Block 7'],
            'block_8': row['Block 8'],
            'diagnosis': row['Diagnosis'],
            'extra_time': row['Extra Time_x'],
            'room': row['Room?'],
            'computer': row['Computer?'],
            'AP_additional_support': row['AP Additional Support (Assessment Accomodation)'],
            'AP_additional_strategies': row['AP Additional Strategies'],
            'overview': row['Overview'],
            'other_concerns': row['Other Concerns'],
            'ELL_extra_time': row['Extra Time_y'],
            'ELL_IB_approved': row['ELL IB Approved?'],
            'dictionary': row['Dictionary?'],
            'ELL_additional_notes': row['ELL Additional Notes'],
        }
        student = Student(**student_dict)
        db.session.add(student)
    db.session.commit()
    print('Successfully added to db!')


@app.route('/')
def home():
    return 'hello world'

@app.route('/test')
def test():
    return render_template('teacher/test_form.html')

from .blueprints.teacher import teacher
app.register_blueprint(teacher)

# flask --app Test-Centre --debug  run

