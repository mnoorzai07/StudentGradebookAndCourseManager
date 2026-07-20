# Student Gradebook and Course Manager

## Full Name

Madina Noorzai

---

## Project Title

### Student Gradebook and Course Manager

---

## Project Description

This project is a Student Gradebook and Course Management System developed in Python using Object-Oriented Programming (OOP). It allows users to create students and courses, enroll students in courses, add assessments (Quiz, Exam, and Project), record grades, calculate averages, and generate a report showing grades and pass/fail status.

---

## How to Run the Project

1. Open the project in Pycharm.
2. Make sure all python files are in the same project folder.
3. Make sure the files and classes are complete.
4. In the main.py you can run the codes. You can add student, add course, enroll student in the course, and other things that are mentioned in the description.

---

## Classes Created

- Student
- Course
- Assessment
- Quiz
- Exam
- Project
- Gradebook

---

## Object-Oriented Programming(OOP) Concepts

### Encapsulation

### Encapsulation
Encapsulation is used in the Student class to control access to the email attribute. The set_email() method validates and updates the email, and get_email() safely returns and gets it.

### Inheritance

The Quiz, Exam, and Project classes inherit from the Assessment class. They reuse the common attributes and methods of the parent class.

### Method Overriding

The Quiz, Exam, and Project classes override the grade_message() and display_info() methods from the Assessment class to return their own assessment message and information.

---

### Custom Features

#### Letter Grades
The get_letter_grade() method converts students' average scores into letter grades (A, B, C, D, E, or F) to make the results easier to understand.

#### Teacher Comments
The get_teacher_comment() method allows teachers to add and display short comments about a student's performance or average score.