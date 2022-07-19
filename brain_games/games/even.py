from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_answer():
    question_number = randint(1, 100)
    return question_number, 'no' if question_number % 2 else 'yes'
