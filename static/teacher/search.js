let students = [];
let studentNames = [];

// Fetch all students from the local URL
async function getStudents() {
    try {
        const response = await fetch('/tests/get_students'); // Replace with your actual URL
        if (!response.ok) {
            throw new Error('Failed to fetch students');
        }
        const data = await response.json(); // Assuming the response is JSON
        students = data; // Store the fetched students in the global array
        studentNames = Object.keys(students);
    } catch (error) {
        console.error('Error fetching students:', error);
    }
}

// Call the function to fetch students when the page loads
getStudents();

const searchInput = document.getElementById('student-search');
const autocompleteList = document.getElementById('autocomplete-list');

// Trigger autocomplete suggestions as the user types
searchInput.addEventListener("input", () => {
    const query = searchInput.value.toLowerCase();
    autocompleteList.innerHTML = "";

    if (!query) return;

    // Filter students based on the query
    const filteredStudents = studentNames.filter(student =>
        student.toLowerCase().includes(query)
    );

    // Display the filtered students in the autocomplete list
    filteredStudents.forEach(student => {
        const listItem = document.createElement('li');
        listItem.textContent = student;

        // Add click event listener to update the input field
        listItem.addEventListener('click', () => {
            searchInput.value = student;
            autocompleteList.innerHTML = ""; // Clear the list after selection
        });

        autocompleteList.appendChild(listItem);
    });
});

const addStudentForm = document.getElementById('add-student-form');

async function sendData(formData) {  
    const url = window.location.href;
    const testId = url.substring(url.lastIndexOf('/') + 1);
    try {
      const response = await fetch(`/tests/add_student/${testId}`, {
        method: "POST",
        // Set the FormData instance as the request body
        body: formData,
      })
      .then((response) => {
        window.location.reload();
      })
      .catch((error) => {
        alert('Error:', error);
      });
    } catch (e) {
      console.error(e);
    }
  }
  

addStudentForm.addEventListener('submit', async (event) => {
    event.preventDefault()
    console.log(students);
    const formData = new FormData(addStudentForm);
    const studentName = formData.get('student-search');
    const studentId = students[studentName]; // Get the student ID using the name
    if (!studentId) {
        alert('Student not found!');
        return;
    }

    // Replace "student-search" with "student_id"
    formData.delete('student-search');
    formData.append('student_id', studentId);
    sendData(formData);

})
