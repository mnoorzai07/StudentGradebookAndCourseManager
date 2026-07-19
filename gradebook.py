class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_course(self, course):
        self.courses[course.course_code] = course


    def enroll_student(self, student_id, course_code):

        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        if student_id not in self.grades:
            self.grades[student_id] = {}

        self.grades[student_id][course_code] = {}



    def add_assessment(self, course_code, assessment):

        if course_code not in self.courses:
            print("Course not found.")
            return

        self.courses[course_code].add_assessment(assessment)

    def record_grade(self, student_id, course_code, assessment_title, score):

        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        assessment = self.courses[course_code].find_assessment(assessment_title)

        if assessment is None:
            print("Assessment not found.")
            return

        percentage = assessment.calculate_percentage(score)

        self.grades[student_id][course_code][assessment_title] = percentage

    def calculate_average(self, student_id, course_code):

        scores = self.grades[student_id][course_code].values()

        if len(scores) == 0:
            return 0

        return sum(scores) / len(scores)

    def get_result(self, average):

        if average >= self.passing_grade:
            return "Passed"

        return "Failed"

    def search_student(self, keyword):

        for student in self.students.values():

            if student.student_id == keyword:
                return student

            if student.name.lower() == keyword.lower():
                return student

        return None

    def delete_student(self, student_id):

        if student_id not in self.students:
            return

        del self.students[student_id]

        if student_id in self.grades:
            del self.grades[student_id]

    def show_report(self, student_id):

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        print(f"Student ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Email: {student.get_email()}")

        print()

        for course_code in self.grades[student_id]:

            course = self.courses[course_code]

            print(f"Course: {course.course_code} - {course.course_name}")
            print()

            print("Grades:")

            for title, grade in self.grades[student_id][course_code].items():
                print(f"{title}: {grade:.1f}%")

            average = self.calculate_average(student_id, course_code)

            print()
            print(f"Average: {average:.1f}%")
            print(f"Result: {self.get_result(average)}")

