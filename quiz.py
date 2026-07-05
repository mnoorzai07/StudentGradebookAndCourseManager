# quiz.py
from assessment import Assessment

class Quiz(Assessment):
    def init(self, title, max_score):
        super().__init__(title, max_score)

    def grade_message(self, score):
        pass

    def display_info(self):
        pass