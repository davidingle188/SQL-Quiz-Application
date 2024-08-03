class Question:
    def __init__(self, question, options, correct_answer, explanation):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

    def check_answer(self, user_answer):
        return self.correct_answer == user_answer  

    def get_explanation(self):
        return self.explanation