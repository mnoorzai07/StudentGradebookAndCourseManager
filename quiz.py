from assessment import Assessment

class Quiz(Assessment):
    def display_info(self):
        print(f"Quiz: {self.title} - Maximum Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 80:
            return "Perfect quiz result!"
        elif 79 >= percentage >= 60:
            return "Good quiz result!"
        else:
            return "Unsatisfying quiz result! Try more!"
