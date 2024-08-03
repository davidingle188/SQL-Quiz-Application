class Quiz:
    def __init__(self, question_list, user_name):
        self.user_name = user_name
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        print("\n" + current_question.question)
        for key, value in current_question.options.items():
            print(f"{key}: {value}")
        self.question_number += 1
        user_input = input('Your answer: ').strip().upper()
        self.check_answer(user_input, current_question.correct_answer)
        print(f"Explanation: {current_question.get_explanation()}")

    def check_answer(self, user_input, correct_answer):
        if user_input == correct_answer:
            print("Your answer is correct!")
            self.score += 1
        else:
            print(f"Wrong answer. The correct answer was {correct_answer}.")