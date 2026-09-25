🎓 Student Admission & Statistics

A Python command-line program that manages student grades, calculates weighted admission scores, determines admission status, and generates overall class statistics.

The program collects grades in Math, Python, and Physics, calculates an admission score using different weights, and then generates a complete report for all students.

🚀 Features
👨‍🎓 Enter multiple students
📐 Enter Math, Python, and Physics grades
⚖️ Calculate a weighted admission score
✅ Determine whether a student is admitted
📋 Generate a complete student report
📊 Calculate the class average
🏆 Find the student with the highest score
👥 Count admitted and non-admitted students
📐 Admission Score

The admission score is calculated using the following formula:

Admission Score =
(Math × 2 + Python × 3 + Physics × 1) / 6
Admission Rule
Score >= 10  → Admitted
Score < 10   → Not admitted
🛠️ Technologies
Python 3
Dictionaries
Nested dictionaries
for loops
if / elif / else
User input
Variables and counters
Mathematical calculations
Formatted strings (f-strings)
▶️ How to Run

Make sure Python 3 is installed on your computer.

Clone the repository:

git clone https://github.com/YOUR-USERNAME/student-admission-statistics.git

Go to the project folder:

cd student-admission-statistics

Run the program:

python student_report.py
💻 Example
enter the number of students: 3

enter the name of the student: Ahmed
enter the math note of the student: 15
enter the python note of the student: 17
enter the physics note of the student: 14

Ahmed is Admitted
Ahmed result is 15.833

enter the name of the student: Sara
enter the math note of the student: 9
enter the python note of the student: 11
enter the physics note of the student: 10

Sara is Admitted
Sara result is 10.333

enter the name of the student: Youssef
enter the math note of the student: 7
enter the python note of the student: 8
enter the physics note of the student: 9

Youssef is Not admitted
Youssef result is 7.833

---------STUDENT REPORT---------

Ahmed :
{'math': 15.0, 'python': 17.0, 'physics': 14.0,
'status': 'Admitted', 'score': 15.833}

Sara :
{'math': 9.0, 'python': 11.0, 'physics': 10.0,
'status': 'Admitted', 'score': 10.333}

Youssef :
{'math': 7.0, 'python': 8.0, 'physics': 9.0,
'status': 'Not admitted', 'score': 7.833}

========== CLASS STATISTICS ==========

Number of students: 3
Class average: 11.333
Best student: Ahmed
Best average: 15.833
Admitted: 2
Not admitted: 1
📚 What I Learned

Through this project, I practiced:

Storing structured data using dictionaries
Using nested dictionaries to organize student information
Calculating weighted averages
Using loops to process multiple students
Using conditions to determine admission status
Keeping counters for different categories
Finding the highest score
Calculating class statistics
Formatting numerical results with :.3f
Building a complete data-processing program with Python

abderrahim bouqoufi
