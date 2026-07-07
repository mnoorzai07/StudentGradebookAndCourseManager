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
        if student_id in self.students:
            student = self.students[student_id]
            student.enroll_course(course_code)
        elif course_code in self.courses:
            course = self.courses[course_code]
            course.enroll_student(student_id)
        else:
            print("Student or Course not found.")

    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)
        else:
            print("Course not found.")

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id not in self.students:
            print("Student not found.")
            return
        if course_code not in self.courses:
            print("Course not found.")
            return
        course = self.courses[course_code]
        assessment = course.find_assessments[assessment_title]

        if assessment is None:
            print("Assessment not found.")
            return
        if student_id not in self.grades:
            self.grades[student_id] = {}
        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}
        self.grades[student_id][course_code][assessment_title] = score

    def calculate_average(self, student_id, course_code):
        if student_id in self.grades and course_code in self.grades[student_id]:
            score = self.grades[student_id][course_code]

            if len(score) == 0:
                return 0
            return sum(score) / len(score)
        return 0

    def get_result(self, average):
        if average >= self.passing_grade:
            return "Passed"
        else:
            return "Failed"

    def show_report(self, student_id):
        pass

    def search_student(self, keyword):
        keyword = keyword.lower()
        for student in self.students:
            if keyword == student.student_id or keyword in student.name.lower():
                return student
        return None

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return
        student = self.students[student_id]

        for course_code in student.courses:
            if course_code in self.courses:
                course = self.courses[course_code]
                if student_id in course.students:
                    course.students.remove(student_id)
        if student_id in self.grades:
            del self.grades[student_id]

    def display_info(self):
        print("==== Gradebook Information ====")
        print(f"Students: {len(self.students)}")
        print(f"Courses: {len(self.courses)}")
        print(f"Passing Grade: {self.passing_grade}")