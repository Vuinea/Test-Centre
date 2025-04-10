# Test-Centre

This project is a management system for Ashbury's test centre. 

## Introduction

TEST-CENTRE is a webapp that works with a database to plan out when students will be taking tests in the test centre and make sure their individual accommodation are handled properly. The IT Department sets up the system and handles backend issues. Teachers use the system to schedule tests for students. Students receive notifications of their tests via email. Test Centre staff use the system to view test schedules and report attendence or problems during tests.


## Getting Started

Download python if it is not already on your system

Clone the repository using `git clone https://github.com/Vuinea/Test-Centre/`

Download required dependencies using `pip install -r requirements.txt`.

Configure the settings to connect the webapp to your desired domain or subdomain.

Run the app using `cd Test-Centre` and then `flask --app app run`

# For Teachers

## Getting Started

Access the TEST-CENTRE at the url provided by your IT department. You will be prompted to login using your credentials.

## Schedule a Test

1. Select "Create Test" from the main menu and fill in the required information.
2. Add students to the test by typing their names into the search box. If a student is not found, you can enter their name manually.
3. Click "Submit" to create the test.

## Edit an Existing Test

1. From the main screen, select a test from the list of upcoming tests. Tests that have already occurred cannot be edited.
2. Change details as needed. In order to remove a student, select the student from the list and click "Remove". In order to add a student, click "+" at the top of the list.
3. Click "Submit" to save your changes.

## Schedule a Make-up Test

Once you have communicated with the student about the date and time they will be able to take the test, simply create a new test using the steps above and add the student to it.

# For Test-Centre Employees

## Getting Started

Access the TEST-CENTRE at the url provided by your IT department. You will be prompted to login using your credentials.

## View Test Schedule

After logging in, you will see a list of upcoming tests. Click a test to view instructions on how to administer the test and details such as which students are expected to take the test and what accommodations they require.

## Report Attendence

In the test detail view, mark each student as present or absent at the start of each test. Click "Submit Attendence Report" when done.

## Report Problems During Test

If for any reason a student is unable to complete the test, edit the attendence report to mark them absent. The teacher will handle rescheduling.

## Contact or Support Info

Contact your IT Department for help if needed.

## User Stories

Teachers want to be able to schedule test for ell/ap and handle students who missed the test quickly and without too much hassle
	- View in the webapp

Test Space Administrators want to be able to reliably know who is taking a test at what time and the details of how long the test runs and what students are allowed for it
	- View in the webapp

School Techs want to be able to look at code and docs to fix problems when they arise 
	- Docs
	- Code
	- Comments

## Planning 

ER Diagram:
![image](https://github.com/user-attachments/assets/a3863474-54fc-4dbf-8742-e1ff5887998c) 

Database Diagram: 
![image](https://github.com/user-attachments/assets/0fecc0e6-9067-4a75-8992-5cd453ac45b8)

User Flow Diagram:
![image](https://github.com/user-attachments/assets/5d0d5270-bbb0-468d-ba31-330f8c6e9b0d)

UI Diagram:
![image](https://github.com/user-attachments/assets/4e44e9e7-df59-4674-8cdc-066446558503)

Whiteboard Sketches:
![image](https://github.com/user-attachments/assets/50a354c6-88bb-46b7-9cab-c4937d9983dc)



