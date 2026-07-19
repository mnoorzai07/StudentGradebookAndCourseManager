from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook


# Create the gradebook
gradebook = Gradebook()


# Add student
student = Student("S001", "Mina Roberts", "minaroberts@gmail.com")

gradebook.add_student(student)



# Add course
course = Course("PY101", "Python Programming")

gradebook.add_course(course)



# Enroll student
gradebook.enroll_student("S001", "PY101")


# Add assessments

quiz = Quiz("Quiz 1", 10)

midterm = Exam("Midterm Exam", 100)

final_project = Project("Final Project", 100)

gradebook.add_assessment("PY101", quiz)
gradebook.add_assessment("PY101", midterm)
gradebook.add_assessment("PY101", final_project)



# Record grades
gradebook.record_grade(
    "S001", "PY101", "Quiz 1", 3)

gradebook.record_grade("S001", "PY101", "Midterm Exam", 40)

gradebook.record_grade("S001", "PY101", "Final Project", 30)



# Calculate average
average = gradebook.calculate_average("S001", "PY101")

print(f"Average: {average:.2f}%")



# Show report
gradebook.show_report("S001")