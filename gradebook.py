class Gradebook:
    def __init__(self, passing_grade):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = passing_grade

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_course(self, course):
        self.courses[course.course_code] = course

    def enroll_student(self, student_id, course_code):
        pass

    def add_assessment(self, course_code, assessment):
        pass

    def record_grade(self, student_id, course_code, assessment_title, score):
        pass

    def calculate_average(self, student_id, course_code):
        pass

    def get_result(self, average):
        pass

    def show_report(self, student_id):
        pass

    def search_student(self, keyword):
        pass

    def delete_student(self, student_id):
        pass

    def display_info(self):
        print("==== Gradebook Information ====")
        print(f"Students: {len(self.students)}")
        print(f"Courses: {len(self.courses)}")
        print(f"Passing Grade: {self.passing_grade}")