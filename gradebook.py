class Gradebook:
    def __init__(self, passing_grade):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = passing_grade

    def add_student(self, student):
        pass

    def add_course(self, course):
        pass

    def enroll_student(self, student_id, course_code):
        pass

    def add_assessment(self, course_code, assessment):
        pass

    def record_grade(self, student_id, course_code, assessment_title, score):
        pass

    def calculate_average(self, student_id, course_code):
        pass