from assessment import Assessment

class Exam(Assessment):

    def display_info(self):
        print(f"Exam: {self.title} - Maximum Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 55:
            return "Passed exam."
        else:
            return "Failed exam."

