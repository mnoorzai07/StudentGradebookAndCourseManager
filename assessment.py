class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 90:
            return "Outstanding Excellent!!!"
        elif 89 >= percentage >= 80:
            return "High Excellence!!!"
        elif 79 >= percentage >= 70:
            return "Above Average!"
        elif 69 >= percentage >= 50:
            return "Average!"
        else:
            return"Developing! You need significant improvement and focus."


    def display_info(self):
        print(f"{self.title}: - Max Score: {self.max_score}")