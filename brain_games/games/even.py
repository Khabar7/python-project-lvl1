from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_question():
    number = randint(1, 100)
    return number, 'no' if number % 2 else 'yes'
