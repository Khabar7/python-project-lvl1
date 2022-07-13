from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    counter = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter = counter + 1
    if counter <= 0:
        return True
    else:
        return False


def make_question():
    number = randint(1, 100)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer
