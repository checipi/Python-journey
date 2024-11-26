from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

# My Code

question_bank = []
quizz_brain = QuizzBrain(question_bank)

# question_bank = [Question(q_text=q['text'], q_answer=q['answer']) for q in question_data]

# for q in question_data:
#    # print(q['text'],"\n",q['answer'])
#     question_bank.append(Question(q['text'], q['answer']))

for q in question_data:
    question_text = q['question']
    question_answer = q['correct_answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
    

while quizz_brain.still_has_questions():
    quizz_brain.next_question()
    


# print(question_bank[0].text, question_bank[1].answer)
# print(*question_bank, sep="\n")

