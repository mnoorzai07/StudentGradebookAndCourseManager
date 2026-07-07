class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []

    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def set_email(self, email):
        if "@" in email:
            self.email = email
        else:
            print("Invalid email address!")

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Courses: {self.courses}")