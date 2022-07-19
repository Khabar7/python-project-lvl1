import math
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    if number in [2, 3]:
        return True
    if number % 6 != 5 and number % 6 != 1:
        return False
    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if (number % i == 0) or (number % (i + 2) == 0):
            return False
    return True


def get_question_and_answer():
    question_number = randint(1, 100)
    answer = 'yes' if is_prime(question_number) else 'no'
    return question_number, answer
