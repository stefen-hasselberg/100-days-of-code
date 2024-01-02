from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = [Question(q["text"], q["answer"]) for q in question_data]


quizz = QuizzBrain(question_bank)


while quizz.still_has_questions():
    quizz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quizz.score}/{quizz.question_number}")