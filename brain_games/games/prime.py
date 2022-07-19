from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    counter = 3
    for i in range(2, number // 2):
        if number % counter == 0:
            return False
        counter += 2

    return True


def get_question_and_answer():
    question_number = randint(1, 100)
    answer = 'yes' if is_prime(question_number) else 'no'
    return question_number, answer
