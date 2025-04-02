import os
import pandas as pd
from .models import db, Student

def load_data_from_excel(file_path):
    xl = pd.ExcelFile(file_path)
    students_df = xl.parse("Students",
                           converters={
                                        "First Name": str, 
                                        "Preferred": str, 
                                       "Surname": str,
                                        'TAG teacher': str,
                                       'Block 1': str,
                                       'Block 2': str,
                                       'Block 3': str,
                                        'Block 4': str,
                                        'Block 5': str,
                                        'Block 6': str,
                                        'Block 7': str,
                                        'Block 8': str,
                                    })
    ap_df = xl.parse("AP", 
                     converters={
                        'First Name': str, 
                        'Preferred': str, 
                        'Surname': str,
                        'Diagnosis': str,
                        'Extra Time': str,
                        'Room': str,
                        'Computer': str,
                        'AP Additional Support (Assessment Accomodation)': str,
                        'AP Additional Strategies': str,
                        'Overview': str,
                        'Other Concerns': str
                    })
    ell_df = xl.parse("ELL", 
                      converters={
                        'First Name': str, 
                        'Surname': str,
                        'Extra Time': str,
                        'ELL IB Approved': str,
                        'Dictionary': str,
                        'ELL Additional Notes': str
                      })
    return students_df, ap_df, ell_df

# I merged all the data tabs into one list if names matched, so the database doesn't have different tabs

def merge_data(students_df: pd.DataFrame, ap_df: pd.DataFrame, ell_df: pd.DataFrame):
    merged_df = students_df.copy()
    ap_df.drop_duplicates(subset=["First Name", "Surname"], keep='first', inplace=True)
    merged_df = pd.merge(merged_df, ap_df, on=["First Name", "Preferred", "Surname"], how='left')

    #ell data merge
    ell_df.drop_duplicates(subset=["first name", "surname"], keep='first', inplace=True)
    merged_df = pd.merge(merged_df, ell_df, on=["First Name", "Preferred", "Surname"], how='left')

    merged_df.fillna("", inplace=True)
    return merged_df

def insert_into_database():
    data_path = os.path.join(os.getcwd(), 'instance/ap_ell_master_for_teachers.xlsx')
    data = load_data_from_excel(data_path)
    merged = merge_data(*data)

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

