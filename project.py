from assessment import Assessment

class Project(Assessment):


    def display_info(self):
        print(f"Project: {self.title} - Maximum Score: {self.max_score}")



    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 90:
            return "Excellent project!"
        elif percentage >= 55:
            return "Project submitted."
        else:
            return "Project needs improvement."
