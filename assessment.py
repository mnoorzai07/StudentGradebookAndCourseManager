class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 90:
            return "Outstanding Excellent!!! Absolute mastery and top-tier performance."
        elif 89 >= percentage >= 80:
            return "High Excellence!!! Strong capacity with minor room for growth."
        elif 79 >= percentage >= 70:
            return "Above Average! Meeting the basic requirements, need refinement."
        elif 50 >= percentage >= 69:
            return "Average! You meet the basic requirements,but you need refinement."
        else:
            return"Developing! You need significant improvement and focus."


    def display_info(self):
        print(f"{self.title}: {self.max_score}%")