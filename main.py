from quiz import Quiz
from data import sql_questions
from questions import Question
from asci import art

# Create Question objects
my_questions = [Question(
    value['question'],
    value['options'],
    value['correct_option'],
    value['explanation']
) for value in sql_questions]

# Create Quiz object
print(art())
print('You have to select the correct option from A, B, C, D')
my_quiz = Quiz(my_questions, input("Please enter your name ").capitalize())

# Run the quiz
while my_quiz.still_has_questions():
    my_quiz.next_question()
print(f"{my_quiz.user_name} your current score is {my_quiz.score}/{len(my_quiz.question_list)}")
