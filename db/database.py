import sqlite3
import pandas as pd
from .models import db

def create_database():
    pass
    # conn = sqlite3.connect(db_name)
    # cursor = conn.cursor()
    # # table creating the student
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS Students (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         first_name TEXT,
    #         preferred TEXT,
    #         surname TEXT,
    #         TAG_teacher TEXT,
    #         block_1 TEXT,
    #         block_2 TEXT,
    #         block_3 TEXT,
    #         block_4 TEXT,
    #         block_5 TEXT,
    #         block_6 TEXT,
    #         block_7 TEXT,
    #         block_8 TEXT,
    #         diagnosis TEXT,
    #         extra_time TEXT,
    #         room TEXT,
    #         computer TEXT,
    #         AP_additional_support TEXT,
    #         AP_additional_strategies TEXT,
    #         overview TEXT,
    #         other_concerns TEXT,
    #         ELL_extra_time TEXT,
    #         ELL_IB_approved TEXT,
    #         dictionary TEXT,
    #         ELL_additional_notes TEXT
    #     )
    # """)
    # conn.commit()
    # conn.close()

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

#i merged all the data tabs into one list if names matched, so the database doesnt have different tabs

def merge_data(students_df: pd.DataFrame, ap_df: pd.DataFrame, ell_df: pd.DataFrame):
    merged_df = students_df.copy()
    # print(students_df['First Name'].dtype)
    # print(ap_df['First Name'].dtype)
    # print(ell_df['First Name'].dtype)
    # print(students_df['Preferred'].dtype)
    # print(ap_df['Preferred'].dtype)
    # print(ell_df['Preferred'].dtype)
    #ap data merge
    ap_df.drop_duplicates(subset=["First Name", "Surname"], keep='first', inplace=True)
    merged_df = pd.merge(merged_df, ap_df, on=["First Name", "Preferred", "Surname"], how='left')

    #ell data merge
    ell_df.drop_duplicates(subset=["first name", "surname"], keep='first', inplace=True)
    merged_df = pd.merge(merged_df, ell_df, on=["First Name", "Preferred", "Surname"], how='left')

    merged_df.fillna("", inplace=True)
    return merged_df

def insert_into_database(merged_df: pd.DataFrame):
    pass


    # conn = sqlite3.connect(db_name)
    # cursor = conn.cursor()

    # for _, row in merged_df.iterrows():
    #     cursor.execute("""
    #         INSERT INTO Students (
    #             first_name, preferred, surname, TAG_teacher, block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8,
    #             diagnosis, extra_time, room, computer, AP_additional_support, AP_additional_strategies, overview, other_concerns,
    #             ELL_extra_time, ELL_IB_approved, dictionary, ELL_additional_notes
    #         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    #     """, tuple(row))

    # conn.commit()
    # conn.close()

def main():
    db_name = "students.db"
    excel_file = "students_data.xlsx"

    create_database(db_name)
    students_df, ap_df, ell_df = load_data_from_excel(excel_file)
    merged_df = merge_data(students_df, ap_df, ell_df)
    insert_into_database(merged_df, db_name)

    print("Database has been successfully created and populated.")

if __name__ == "__main__":
    main()