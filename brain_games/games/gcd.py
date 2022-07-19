from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question_number = f'{num1} {num2}'
    answer = gcd(num1, num2)
    return question_number, str(answer)


def gcd(num1, num2):
    if not num2:
        return num1
    return gcd(num2, num1 % num2)
