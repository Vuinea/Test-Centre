# Test-Centre

This project is a management system for Ashbury's test centre. 

## Introduction

TEST-CENTRE is a webapp that works with a database to plan out when students will be taking tests in the test centre and make sure their individual accommodation are handled properly. The IT Department sets up the system and handles backend issues. Teachers use the system to schedule tests for students. Students receive notifications of their tests via email. Test Centre staff use the system to view test schedules and report attendence or problems during tests.

### For IT Department

TEST-CENTRE requires Python.

## Getting Started

Clone the repository using `git clone https://github.com/Vuinea/Test-Centre/`

Download required dependencies using `pip install -r requirements.txt`.

Configure the settings to connect the webapp to your desired domain or subdomain.

Run the app using `flask --app Test-Centre run`

## Troubleshooting

The app might not run
the settings might be wrong
try running with debug flag

# For Teachers

## Getting Started

Access the TEST-CENTRE at the url provided by your IT department. You will be prompted to login using your Microsoft credentials.

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

# For Students

Students will not use TEST-CENTRE directly. They will receive notifications from the system via their school email.

# For Test-Centre Employees

## Getting Started

Access the TEST-CENTRE at the url provided by your IT department. You will be prompted to login using your Microsoft credentials.

## View Test Schedule

After logging in, you will see a list of upcoming tests. Click a test to view instructions on how to administer the test and details such as which students are expected to take the test and what accommodations they require.

## Report Attendence

In the test detail view, mark each student as present or absent at the start of each test. Click "Submit Attendence Report" when done.

## Report Problems During Test

If for any reason a student is unable to complete the test, edit the attendence report to mark them absent. The teacher will handle rescheduling.

# Contact or Support Info

Contact your IT Department for help if needed.
